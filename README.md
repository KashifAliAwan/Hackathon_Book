# Qwen Re-Authentication Guide (New Gmail Account)

Ye guide un students ke liye hai jinka Qwen token full ho gaya ho aur wo naya account (new Gmail) se login karna chahte hon Claude Code Router ke sath.

---

## Step 1: Purani Authentication File Delete Karo

Is path par jao:

C:\Users\Computer ka Name\.qwen Folder hoga usy open kro 

Is file ko delete karo:

oauth_creds.json

> Ye step zaroori hai warna naya account authenticate nahi hoga.

---

## Step 2: PowerShell Open Karo

Start Menu open karo  
PowerShell likho aur open karo (Admin is better)

---

## Step 3: Qwen Command Run Karo

PowerShell me yeh command run karo:

qwen

Terminal pooche ga authentication kis service se karni hai:

- OpenAI
- QwenAuth (Auth kr ka kuch ay ga )

Yahan **Auth wala  select karo**.

---

## Step 4: Browser Me New Gmail Se Login Karo

- Browser open ho jaye ga
- Qwen login page ayega
- New Gmail se login karo
- Permissions allow karo
- Login success hone ke baad browser band kar do
- phir jao yhn C:\Users\Computer ka Name\.qwen Folder ka under wo jo file delete ki thi dubra generate ho gai hogi (oauth_creds.json) File Open kro
  whn :
    {
  "access_token": "wnHfdYGgK0-MHN5mVSu0VfzsKCQ93l0yP7vxlp_K47LAMPmIhYrY7nwrBT76JIok1Ie5rQ", -> Is trh ki Api ya access token show ho rha hoga copy kryn aesy 
  "refresh_token": "O9XqAqIBBn-adSRRjQ170hQ5k1--qHGApEfBBXxbCIVat6kH0BmwmEcjoXXRdbqRDcA", 
  "token_type": "Bearer",
  "resource_url": "portal.qwen.ai",
  "expiry_date": 1765215700466
   }

Copy krny ka bad ap a jay claude-code-router ki folder ma jis ki location C:\Users\Computer ka Name\claude-code-router is ka under config.json mojood hogi
file ko kholy usma code hoga

{  
  "LOG": true,  
  "LOG_LEVEL": "info",  
  "HOST": "127.0.0.1",  
  "PORT": 3456,  
  "API_TIMEOUT_MS": 600000,  
  "Providers": [  
    {  
      "name": "qwen",  
      "api_base_url": "https://portal.qwen.ai/v1/chat/completions",  
      "api_key": "wnHfdYGL-0ogK0-MHN5yn6eP7vxlp_K47LAMPmIhYrY7nwrBRXzDknJIok1Ie5rQ",  ____ (Yhn pr ap Apna apki daly jo apny oauth_creds.json yhn sy copy ki )
      "models": [  
        "qwen3-coder-plus",  
        "qwen3-coder-plus",  
        "qwen3-coder-plus"  
      ]  
    }  
  ],  
  "Router": {  
    "default": "qwen,qwen3-coder-plus",  
    "background": "qwen,qwen3-coder-plus",  
    "think": "qwen,qwen3-coder-plus",  
    "longContext": "qwen,qwen3-coder-plus",  
    "longContextThreshold": 60000,  
    "webSearch": "qwen,qwen3-coder-plus"  
  }  
}

or phir ab neachy diye gay steps 

---

## Step 5: New PowerShell Open Karo

Purani PowerShell close karo  
Dobara new PowerShell open karo

---

## Step 6: Claude Code Router Restart Karo

Command run karo:

ccr restart

---

## Step 7: Claude Code Open Karo

Command:

ccr code

---

## Step 8: Test Karo

Claude Code open hone ke baad type karo:

hi

Agar response aa gaya → ✅ Setup working!

---

## Done ✅

Ab aap Qwen naya account ke sath use kar sakte ho.
