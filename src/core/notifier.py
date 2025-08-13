"""
notifier.py
Notificaciones nativas:
- Windows: PowerShell + Windows.UI.Notifications
- macOS: AppleScript
- Linux: notify-send (libnotify)
"""

import subprocess
import platform
import utils.logger as logger

def _ps_escape(text: str) -> str:
    """Escapa comillas para PowerShell (dobles a backtick-quoted)."""
    return text.replace('"', '`"')

def notify(title: str, message: str):
    system = platform.system()
    try:
        if system == "Windows":
            # PowerShell toast basado en Windows Runtime APIs
            title_ps = _ps_escape(title)
            message_ps = _ps_escape(message)
            powershell_script = f"""
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
$textNodes = $template.GetElementsByTagName('text')
$textNodes.Item(0).AppendChild($template.CreateTextNode('{title_ps}')) > $null
$textNodes.Item(1).AppendChild($template.CreateTextNode('{message_ps}')) > $null
$toast = [Windows.UI.Notifications.ToastNotification]::new($template)
$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Generic Discord RPC')
$notifier.Show($toast)
"""
            subprocess.Popen(["powershell", "-NoProfile", "-Command", powershell_script], shell=True)

        elif system == "Darwin":  # macOS
            subprocess.run(['osascript', '-e', f'display notification "{message}" with title "{title}"'])

        elif system == "Linux":
            subprocess.run(['notify-send', title, message])

        else:
            logger.log(f"Sistema operativo no soportado para notificaciones: {system}")

    except Exception as e:
        logger.log(f"Error mostrando notificación: {e}")
