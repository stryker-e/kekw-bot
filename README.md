# kekw-bot
Discord bot that listens for a <strong>":kekw:"</strong> message and sends a <strong>":kekw:"</strong> message back. For its intended purpose, the server must have a custom emote tagged as <strong>:kekw:</strong>. 

This bot can be used for any custom emote by replacing <strong>kekw_id</strong> with any custom emote id. This bot can't be used for standard emojis and unicode characters.

<h3>To edit for your server</h3>
<ol>
  <li>Send <strong>"\:kekw:"</strong> in a message to your server in any channel. Your message will be echoed, edited as <:kekw:[id number]>.</li>
  <li>In main.py, replace kekw_id with the string for your server's :kekw: custom emote id.</li>
  <li>Edit the .env file to set <strong>DISCORD_BOT</strong>=[server token]</li>
