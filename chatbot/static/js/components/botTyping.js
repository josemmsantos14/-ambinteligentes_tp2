/**
 * removes the bot typing indicator from the chat screen
 */
function hideBotTyping() {
  $("#botAvatar").remove();
  $(".botTyping").remove();
}

/**
 * adds the bot typing indicator from the chat screen
 */
function showBotTyping() {
  const botTyping =
    '<img class="botAvatar" id="botAvatar" src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSICoxyj5LqnljK7sK0rk4l32QMHCFzCH7D8wBmcPGQIq8M8jnv"/><div class="botTyping"><div class="bounce1"></div><div class="bounce2"></div><div class="bounce3"></div></div>';
  $(botTyping).appendTo(".chats");
  $(".botTyping").show();
  scrollToBottomOfResults();
}
