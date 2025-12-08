# Qwen Re-Authentication Guide (New Gmail Account)

Ye guide un students ke liye hai jinka Qwen token full ho gaya ho aur wo naya account (new Gmail) se login karna chahte hon Claude Code Router ke sath.

---

## Step 1: Purani Authentication File Delete Karo

Is path par jao:

C:\Users\YOUR_USERNAME\.qwen

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
- Qwen

Yahan **Qwen select karo**.

---

## Step 4: Browser Me New Gmail Se Login Karo

- Browser open ho jaye ga
- Qwen login page ayega
- New Gmail se login karo
- Permissions allow karo
- Login success hone ke baad browser band kar do

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
