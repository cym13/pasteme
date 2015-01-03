% rebase('base.tpl', title='Paste snippets')

<div id="timeleft">
  This file will be deleted on {{!timeleft}}
</div>

{{!content}}
<div id="floatingmenu">
  <a href="/"><img alt="return" src="static/esc-icon.png" /></a><br />
  <a href="/{{pid}}/raw"><img alt="raw" src="static/download-icon.png" /></a>
</div>
