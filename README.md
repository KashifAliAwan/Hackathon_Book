# ✅ Qwen Re-Authentication Guide (New Gmail Account)

Ye guide un students ke liye hai jinka **Qwen access token full** ho gaya ho aur jo **naye Gmail account** se Qwen ko Claude Code Router ke sath re-authenticate karna chahte hain.

---

## 🧹 Step 1: Purani Authentication File Delete Karo

Is path par jao:

```
C:\Users\COMPUTER_NAME\.qwen
```

Is file ko delete karo:

```
oauth_creds.json
```

> ⚠️ Ye step bohat zaroori hai. Agar ye file delete na hui, to naya account authenticate nahi hoga.

---

## ⚡ Step 2: PowerShell Open Karo

1. Start Menu open karo  
2. Type karo: `PowerShell`  
3. Open karo (Admin mode recommended)

---

## ▶️ Step 3: Qwen Command Run Karo

PowerShell me ye command run karo:

```
qwen
```

Terminal pooche ga authentication kis service se karni hai:

- OpenAI  
- QwenAuth  

👉 YNote: **QwenAuth select karo**.

---

## 🌐 Step 4: Browser Me New Gmail Se Login Karo

1. Browser automatically open ho jaye ga  
2. Qwen login page ayega  
3. **New Gmail account se login karo**  
4. Permissions allow karo  
5. Login hone ke baad browser close kar do  

Ab dubara jao:

```
C:\Users\COMPUTER_NAME\.qwen
```

Yahan ye file dobara generate ho chuki hogi:

```
oauth_creds.json
```

Is file ko open karo. Aap ko is tarah ka data mile ga:

```json
{
  "access_token": "xxxxxxx",
  "refresh_token": "xxxxxxx",
  "token_type": "Bearer",
  "resource_url": "portal.qwen.ai",
  "expiry_date": 1765215700466
}
```

👉 Yahan se `access_token` copy kar lo.

---

## ⚙️ Step 5: Claude Code Router Me Token Update Karo

Is folder me jao:

```
C:\Users\COMPUTER_NAME\claude-code-router
```

Wahan file open karo:

```
config.json
```

Is code me:

```json
"api_key": "YOUR_OLD_TOKEN_HERE"
```

Iski jagah apna **naya access_token** paste karo:

```json
"api_key": "PASTE_YOUR_NEW_ACCESS_TOKEN_HERE"
```

Save file ✅

---

## 🔁 Step 6: New PowerShell Open Karo

- Purani PowerShell close karo  
- New PowerShell open karo

---

## 🔄 Step 7: Claude Code Router Restart Karo

Command run karo:

```
ccr restart
```

---

## ▶️ Step 8: Claude Code Open Karo

Command:

```
ccr code
```

---

## ✅ Step 9: Test Karo

Claude Code open hone ke baad type karo:

```
hi
```

Agar response aa gaya → ✅ **Setup Successful!**

---

## 🎉 Done!

Ab aap Qwen ko naye Gmail account ke sath successfully use kar sakte ho.

---

### 📌 Notes:
- Agar issue aaye:
  - `oauth_creds.json` delete ki thi ya nahi check karo  
  - Correct token `config.json` me paste hua ho  
  - `ccr restart` properly run hua ho  

---

Happy Coding 🚀
