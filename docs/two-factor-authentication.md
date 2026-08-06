# Two-Factor Authentication

Scarf supports time-based one-time passwords (TOTP) from authenticator apps. Two-factor authentication adds a passcode check after you enter your password.

## Enable two-factor authentication

1. Sign in to [Scarf](https://app.scarf.sh) and open your account settings.
2. Find **Two-factor authentication** and select **Enable**.
3. Scan the QR code with an authenticator app.
4. Save the recovery codes in a secure location.
5. Enter the passcode from your authenticator app to finish setup.

Scarf shows the recovery codes once during setup. Each code can replace an authenticator passcode for one login.

## Sign in with two-factor authentication

After you enter your username and password, enter the current passcode from your authenticator app.

If you cannot access the app, enter one of your unused recovery codes. Scarf replaces your recovery-code set after you use the final code. Save the new codes before you dismiss the message because Scarf will not show them again.

## Reset two-factor authentication

Reset two-factor authentication when you move to a new device or need a new authenticator secret:

1. Open your account settings.
2. Select the option to reset two-factor authentication.
3. Verify your identity with a current authenticator passcode or an unused recovery code.
4. Scan the new QR code.
5. Save the new recovery codes.
6. Enter a passcode from the new authenticator setup.

Resetting two-factor authentication invalidates the previous authenticator secret and recovery codes.

If you lose access to both your authenticator app and every recovery code, contact [Scarf support](mailto:support@scarf.sh).
