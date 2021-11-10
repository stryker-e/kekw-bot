# kekw-bot
Discord bot that listens for a <strong>":kekw:"</strong> message and sends a <strong>":kekw:"</strong> message back. For its intended purpose, the server must have a custom emote tagged as <strong>:kekw:</strong>. 

This bot can be used for any custom emote by replacing <strong>kekw_id</strong> with any custom emote id. This bot can't be used for standard emojis and unicode characters.

<h3>Bot Commands</h3>
<ul>
  <li><strong>!toggle</strong>: turns emoji ping response on and off. When on, the bot activity presence will be "Waiting for emoji ping". When off, the bot activity presence will be "Not waiting for emoji ping", and the bot will ignore all emoji pings and commands except <strong>!toggle</strong>. By default, the bot is on. <strong>Note:</strong> this command is not listed in response to <strong>!help</strong> to aid server management.</li>
  <li><strong>!help</strong>: lists available commands and functions (except <strong>!toggle</strong>)</li>
  <li><strong>!change</strong>: changes which custom emoji to respond to. After sending this command, the user is prompted to enter the emoji alias formatted as <strong>\:emoji_alias:</strong> Initially, the custom emoji id must be set in order to use the bot.</li>
  <li><strong>!check</strong>: returns the id of the current emoji ping</li>
</ul>

<h3>To edit for your server</h3>
Edit the .env file to set <strong>DISCORD_BOT</strong>=[server token]
