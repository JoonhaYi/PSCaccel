from mitmproxy import http

TARGET_JS_PATH = "https://pulsars.nanograv.org/app/components/com_psrsearch/site/assets/js/psrplots.js?v=1743828310"

print("test")

def response(flow: http.HTTPFlow):
    # Only intercept the specific JS file by URL path
    if TARGET_JS_PATH in flow.request.path:
        text = flow.response.get_text()
        
        # Replace the function definition
        modified = text.replace(
            "function isBetaUser() {\n  return false;\n}",
            "function isBetaUser() {\n  return true;\n}"
        )
        
        flow.response.set_text("")
        print(f"[*] Modified {TARGET_JS_PATH}")
