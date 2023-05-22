/* module for importing other js files */
function include(file) {
  const script = document.createElement("script");
  script.src = file;
  script.type = "text/javascript";
  script.defer = true;

  document.getElementsByTagName("head").item(0).appendChild(script);
}

// Bot pop-up intro
document.addEventListener("DOMContentLoaded", () => {
  const elemsTap = document.querySelector(".tap-target");
  // eslint-disable-next-line no-undef
  const instancesTap = M.TapTarget.init(elemsTap, {});
  instancesTap.open();
  setTimeout(() => {
    instancesTap.close();
  }, 4000);
});

/* import components */
include("./static/js/components/index.js");

window.addEventListener("load", () => {
  // initialization
  $(document).ready(() => {
    //............................................................................................
    let urls = [
      "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTgyODk3ZTk2MzBhOWZiNGViMjM1NTVkZWU0ZTcyNThlYWE3ZDI4YiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/Yat5wnwisEV2iXbt4x/giphy.gif",
      "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDcyZDJlYTdhNzdiMDVmYzE1MjJkZGUyMGVjZDIyZDdkMDVhYzM4YyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/V0UVbB1tZCL3ov0Iwx/giphy.gif",
      "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjZiMjdkYzdmYWU5MzA1NzFkZWU4NmI2N2JjZGU3YjMyNTZmODY3NCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/rIdDOeGiIBmzZXsCef/giphy.gif",
      "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzY3NDQ1Mjg5YzQ5MjUzYzcwN2ZkMTNjZjY5YmRkNmFlOTU5ODdmMSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/hxZ5FdXCk2bxT7wKDb/giphy.gif",
    ];
    let bgcolors = ["#ffe6e6", "#fd9889", "#ffddfe", "#5efbe6"];
    let cout = 1;
    $(".container").css("background-image", 'url("' + urls[0] + '")');
    $("body").css("background-color", bgcolors[0]);
    setInterval(function () {
      $(".container").css("background-image", 'url("' + urls[cout] + '")');
      $("body").css("background-color", bgcolors[cout]);
      cout == urls.length - 1 ? (cout = 0) : cout++;
    }, 5000);
    //............................................................................................

    // Bot pop-up intro
    $("div").removeClass("tap-target-origin");

    // drop down menu for close, restart conversation & clear the chats.
    $(".dropdown-trigger").dropdown();

    // initiate the modal for displaying the charts,
    // if you dont have charts, then you comment the below line
    $(".modal").modal();

    // enable this if u have configured the bot to start the conversation.
    // showBotTyping();
    // $("#userInput").prop('disabled', true);

    // if you want the bot to start the conversation
    // customActionTrigger();
  });
  // Toggle the chatbot screen
  $("#profile_div").click(() => {
    $(".profile_div").toggle();
    $(".widget").toggle();
  });

  // clear function to clear the chat contents of the widget.
  $("#clear").click(() => {
    $(".chats").fadeOut("normal", () => {
      $(".chats").html("");
      $(".chats").fadeIn();
    });
  });

  // close function to close the widget.
  $("#close").click(() => {
    $(".profile_div").toggle();
    $(".widget").toggle();
    scrollToBottomOfResults();
  });
  $("#close-bot-btn").click(() => {
    $(".profile_div").toggle();
    $(".widget").toggle();
    scrollToBottomOfResults();
  });
});
