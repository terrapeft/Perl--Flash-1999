document.onmouseover = raise;
document.onmouseout = flat;
document.onmousedown = lower;
document.onmouseup = up;

function findChildImage ( el ) {
  var children = el.children;
  for (var i=0; i<children.length; i++) {
    if ( children[i].tagName == "IMG" ) {
	   return(children[i]);
	}
  }
}

function getReal(el, type, value) {
	temp = el;
	while ((temp != null) && (temp.tagName != "BODY")) {
		if (eval("temp." + type) == value) {
			el = temp;
			return el;
		}
		temp = temp.parentElement;
	}
	return el;
}

function raise() {
  var toEl = getReal(window.event.toElement, "className", "complexButton");
  var fromEl = getReal(window.event.fromElement, "className", "complexButton");
  if (toEl == fromEl) return;
  el = toEl;
  if ( el.className == "complexButton" ) {
	  with (el.style) {
		borderLeft   = "1px solid buttonhighlight";
	    borderRight  = "1px solid buttonshadow";
		borderTop    = "1px solid buttonhighlight";
		borderBottom = "1px solid buttonshadow";
		padding      = "1px";		
	    var buttomImg = findChildImage(el);
		if (buttomImg != null) {
		   buttomImg.style.filter = "";
		}
	  }
  }
}

function flat() {
  var toEl = getReal(window.event.toElement, "className", "complexButton");
  var fromEl = getReal(window.event.fromElement, "className", "complexButton");
  if (toEl == fromEl) return;
  el = fromEl;
  if ( el.className == "complexButton" ) {
	  with (el.style) {
	    border = "1px solid buttonface";
		padding = "1px";		
	    var buttomImg = findChildImage(el);
		buttomImg.style.filter = "gray()";	
	  }
  }
}

function lower() {
  el = getReal(window.event.srcElement, "className", "complexButton");
  if (el.className == "complexButton") {
	  with (el.style) {
	    borderLeft   = "1px solid buttonshadow";
	    borderRight  = "1px solid buttonhighlight";
	  	borderTop    = "1px solid buttonshadow";
		borderBottom = "1px solid buttonhighlight";
		paddingTop    = "2px";
	    paddingLeft   = "2px";
		paddingBottom = "0px";
		paddingRight  = "0px";	
	  }
  }
}

function up() {
  el = getReal(window.event.srcElement, "className", "complexButton");
  if (el.className == "complexButton") {  
	  with (el.style) {
		borderLeft   = "1px solid buttonhighlight";
	    borderRight  = "1px solid buttonshadow";
		borderTop    = "1px solid buttonhighlight";
		borderBottom = "1px solid buttonshadow";
	    padding = "1px";			
	  }
  }
}