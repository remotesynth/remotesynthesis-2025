---
title: Adding a Mailing List Subscription with Mailjet and Netlify Functions
description: Mailing lists are expensive! Let's get set up on a cheaper option using Mailjet and a serverless function.
tags:
  - web development
pubDatetime: 2023-08-13T10:23:31.210Z
---

Next week is the 6 year anniversary of [CFE.dev](https://cfe.dev). I probably wouldn't have believed you if you told me when I got started 6 years ago that the single biggest expense to running a site like this would be maintaining a mailing list. That's right, it's not the streaming service (Streamyard) or the virtual event service (Crowdcast) or the hosting (Netlify), it's emails.

I moved from Mailchimp some years back because the cost was going to be a major burden, especially once they changed how they calculate their pricing (anyone you've been in contact with, even if they are unsubscribed and you aren't allowed to communicate with them, counts against your cap). At the time, ActiveCampaign was a cheaper but still full featured option. However, I never really needed all the features (particularly around campaign automation) and it's come time again where I need to move. As it turns out, moving from ActiveCampaign to [Mailjet](https://mailjet.com) gets me the features I need for over $100 less per month.

There are two ways you get subscribed to my mailing list. The first is through an automation built with Zapier that adds you when you register for an event via Crowdcast. The second is via the subscription forms on my site. In this post, I just want to share the code for adding a new contact to Mailjet via a Netlify Function.

## Creating the Netlify Function

Mailjet provides a [JavaScript SDK](https://github.com/mailjet/mailjet-apiv3-nodejs) that actually makes integrating with its API pretty easy. You'll need your Mailjet API key and secret key, which you can find in Mailjet under Account Settings and then choose "API Key Management (Primary and Sub-account)" under REST API. Place those in an environment variable.

One quirk (to me) of Mailjet is that you can have contacts but if they aren't added to a list, then you can't send them campaigns. In order to add them to a list, you'll need the list ID, which you can find under Contacts  and then Contact Lists in your account. I didn't put this in an environment variable, though I could have. It's not sensitive info but that might make it easier to manage. However, it's worth noting that you can have multiple lists and may want to add the user to more than one.

As you'll see in the code below, there's really two steps to the process:

* Add the user to your contacts and get their new user ID.
* Add the user to the appropriate list(s).

Outside of that, the code is pretty simple. Is it weird that I use a `then` and then an `await` within the result? Maybe, but it works and it was easier to wrap my head around.

```javascript
const Mailjet = require("node-mailjet");

const mailjet = new Mailjet({
  apiKey: process.env.MAILJET_API_KEY,
  apiSecret: process.env.MAILJET_SECRET_KEY,
});
const listID = 12345678;

exports.handler = async (event, context, callback) => {
  try {
    if (!event.body) {
      return {
        statusCode: 500,
        body: "email query parameter required",
      };
    }
    const body = JSON.parse(event.body);
    const email = body.email;
    const firstName = body.firstName ? body.firstName : "";
    const lastName = body.lastName ? body.lastName : "";
    if (!email) {
      return {
        statusCode: 500,
        body: "email query parameter required",
      };
    }

    return mailjet
      .post("contact")
      .request({
        Email: email,
        IsExcludedFromCampaigns: false,
        Name: firstName + " " + lastName,
      })
      .then(async (res) => {
        const addedToList = mailjet
          .post("contact")
          .id(res.body.Data[0].ID)
          .action("managecontactslists")
          .request({
            ContactsLists: [
              {
                ListID: listID,
                Action: "addnoforce",
              },
            ],
          });
        const response = { msg: "Good news! You've been added." };
        return {
          statusCode: 200,
          body: JSON.stringify(response),
        };
      })
      .catch((err) => {
        console.log(err);
        const response = { errorMsg: err.response.statusText };
        return {
          statusCode: 200,
          body: JSON.stringify(response),
        };
      });
  } catch (err) {
    console.log(err);
    return { statusCode: 500, body: err.toString() };
  }
};
```

One thing to note is that I am returning the error message from Mailjet if the user wasn't added to the list, but, unlike ActiveCampaign, it's not the most user friendly message. Typically, this is if you are already on the list, but it might be worth checking the messages and responding with something more friendly (it's on my todo list).

## Using the Function

So, CFE is a totally static site, so I need to call this function via client JavaScript. IKR! You can still do that?!? 

Every Netlify function has a URL that you can post to, so it's just a matter of making the HTTP request. The script is pretty simple, it adds a submit event listener to the form, gathers the data and then uses [Axios](https://axios-http.com/) to make the request to the function. Do I need Axios? No, but it works.

```javascript
registerForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let form = e.target;
  let name = form.elements["join-name"].value;
  let email = form.elements["join-email"].value;
  let firstName = "";
  let lastName = "";
  const errorMessage = document.getElementById("errorMessage");

  if (email === "") errorMessage.innerHTML = "Please fill in all fields";

  if (name !== "") {
    const nameArray = name.split(" ");
    if (nameArray.length) firstName = nameArray[0];

    if (nameArray.length > 1) {
      nameArray.shift();
      lastName = nameArray.join(" ");
    }
  }
  axios
    .post("/.netlify/functions/mailjet", {
      email: email,
      firstName: firstName,
      lastName: lastName,
    })
    .then(function (response) {
      if (response.data.errorMsg && errorMessage)
        errorMessage.innerHTML = response.data.errorMsg;
      else if (response.data.msg && errorMessage)
        errorMessage.innerHTML = response.data.msg;
    })
    .catch(function (error) {
      if (errorMessage) {
        errorMessage.innerHTML =
          "The request failed. Please try again in a moment.";
      } else {
        console.log("Failed to login user: %o", error);
        throw error;
      }
    });
});
```

## That's it!

So there's nothing groundbreaking here and there are definitely ways to improve the code (this is a side project, so often "it works" is all I have time for). But if you are running a mailing list and looking to use Mailjet, hopefully this code will help.

P.S. If you notice any issues with the new mailing list form or with the mailing list itself (assuming you're a subscriber), let me know.