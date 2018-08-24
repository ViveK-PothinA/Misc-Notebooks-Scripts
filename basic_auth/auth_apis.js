const express = require("express");
const app = express();
const cors = require("cors");

app.use(cors()); // to send CORS headers.
app.use(express.urlencoded()); // to support URL-encoded bodies.
app.use(express.json()); // to support JSON-encoded bodies.

app.get("/", (_req, res) =>
  res.send(`
  <span>Hello there! This is the root URL. These are the end-points:</span>
  <ul>
    <li>
      <form action="/signup" method="post">
        <input type="hidden" name="email" value="example@example.com" />
        <input type="hidden" name="username" value="example" />
        <input type="hidden" name="password" value="example" />
        <button type="submit">
          <strong>POST</strong> <code>/signup (email="example@example.com" username="example" password="example")</code>
        </button>
      </form>
    </li>
    <li>
      <form action="/login" method="post">
        <input type="hidden" name="email" value="example@example.com" />
        <input type="hidden" name="password" value="example" />
        <button type="submit">
          <strong>POST</strong> <code>/login (email="example@example.com" password="example")</code>
        </button>
      </form>
    </li>
    <li>
      <form action="/reset" method="post">
        <input type="hidden" name="email" value="example@example.com" />
        <input type="hidden" name="username" value="example" />
        <button type="submit">
          <strong>POST</strong> <code>/signup (email="example@example.com" username="example")</code>
        </button>
      </form>
    </li>
  </ul>
  `)
);

// Using simple dictionary to store the data
var data = {};

app.post("/signup", function(req, res){
    // console.log(req.body);
    if(!req.body.hasOwnProperty('email') && !req.body.hasOwnProperty('username') && !req.body.hasOwnProperty('password')){
        res.status(409).send(`<span>Invalid Request, try again!</span>`);
    }
    var email = String(req.body.email).toLowerCase();
    var username = String(req.body.username);
    var password = String(req.body.password);

    // Email validation
    if(!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
        res.status(409).send(`<span>Invalid Email, try again!</span>`);
    }
    // Email availability
    if(data.hasOwnProperty(email)){
        res.status(409).send(`<span>Email already exists, try logging in!</span>`);
    }

    // Basic Password encryption
    password = Buffer.from(password).toString('base64');

    // Storing in the database, in this case, a simple dictionary
    data[email] = {'username': username, 'password':password};

    console.log(data);
    res.status(200).send(`<span>Registration Successful!</span>`);
});

app.post("/login", function(req, res){
    if(!req.body.hasOwnProperty('email') && !req.body.hasOwnProperty('password')){
        res.status(409).send(`<span>Invalid Request, try again!</span>`);
    }
    var email = String(req.body.email).toLowerCase();
    var password = String(req.body.password);

    // Email validation
    if(!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
        res.status(409).send(`<span>Invalid Email, try again!</span>`);
    }
    // Email availability
    if(!data.hasOwnProperty(email)){
        res.status(409).send(`<span>Email doesn't exist, try signing up!</span>`);
    }
    // Encoding password to verify
    var encoded = Buffer.from(password).toString('base64');

    // Password Verification
    if(data[email]['password'] === encoded){
        res.status(200).send(`<span>Welcome `+data[email]['username']+`!</span>`);
    }
    else{
        res.status(409).send(`<span>Email and Password doesn't match up, try again!</span>`);
    }
});

app.post("/reset",  function(req, res){
    if(!req.body.hasOwnProperty('email')){
        res.status(409).send(`<span>Invalid Request, try again!</span>`);
    }
    var email = String(req.body.email).toLowerCase();

    // Email validation
    if(!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
        res.status(409).send(`<span>Invalid Email, try again!</span>`);
    }
    // Email availability
    if(!data.hasOwnProperty(email)){
        res.status(409).send(`<span>Email doesn't exist, try signing up!</span>`);
    }

    // Creating a random Password
    var newPassword = String(Math.floor(100000 + Math.random() * 900000));
    var encodedPassword = Buffer.from(newPassword).toString('base64');

    // Updating the password
    data[email]['password'] = encodedPassword;

    // Send the mail with the new password, in this case, we'll just print the new Password
    res.status(200).send(`<span>Your password has been updated to `+newPassword+`</span>`);

});

app.listen(5000, () => console.log("API is listening on port 5000!"));