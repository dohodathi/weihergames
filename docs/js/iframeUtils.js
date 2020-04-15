console.log('resizeIframe loaded');

function resizeIframe(obj) {
    if (obj.style && obj.contentWindow) {
        obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 'px';
    } else {
        console.error(
            'obj has no property style or contentWindow. The iframe embed should be on the same origin?',
            obj,
        );
    }
}
