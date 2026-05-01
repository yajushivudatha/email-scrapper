function submitItems(){
  const domain = document.querySelector("#domain");
  const website = document.querySelector("#website");
  console.log(domain.value);
  console.log(website.value);
  eel.search_emails(domain.value, website.value)(outputValues);

  domain.value = "";
  website.value = "";

}

function clearResults(){
  emails_divs = document.getElementsByClassName("emails");
  for (let i = 0; i < emails_divs.length; i ++){
    emails_divs[i].parentNode.removeChild(emails_divs[i]);
  }
}

function outputValues(emails) {
  console.log(emails);
  const emailsDiv = document.createElement("div");
  emailsDiv.className = "emails";
  for (let i = 0; i < emails.length; i ++){
    const p = document.createElement("p");
    const item = document.createTextNode(`${i + 1}. | ${emails[i]}`);
    p.appendChild(item);
    emailsDiv.appendChild(p);
  }
  const body = document.querySelector("body");
  body.appendChild(emailsDiv);
}
