/**
 * @author dotnetCarpenter
 * @version 12.9.1
 */
require(["dojo/parser", "dijit/Editor", "dijit/_editor/plugins/ViewSource"]);
//dojo.require("dijit.Editor");
//dojo.require("dijit._editor.plugins.ViewSource");
dojo.require("dojox.editor.plugins.PrettyPrint");	// let's pretty-print our HTML
dojo.require("dojox.editor.plugins.AutoUrlLink");

dojo.ready(function() {
	var textareas = dojo.query("textarea");
	if (textareas && textareas.length) {
		dojo.addClass(dojo.body(), "claro");
		textareas.instantiate(dijit.Editor, {
			plugins : ["bold", "italic", "|", "viewsource", "prettyprint",
				"dijit._editor.plugins.EnterKeyHandling", 'autourllink']
		});
	}
}); 
