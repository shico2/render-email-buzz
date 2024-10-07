bl_info = {
    "name": "Email Notification on Render Complete",
    "blender": (4, 1, 0),  # Minimum Blender version
    "version": (1, 0),  # Version of the add-on
    "author": "Shico",  # Your name
    "description": "Find in the Properties panel under the Scene tab. Uncheck box when testing still image renders to avoid multiple emails.",
    "warning": "Use with caution; ensure email credentials are secured.",  # Any warnings
    "wiki_url": "https://your-documentation-url.com",
    "category": "Render",  # Category for the add-on
    "support": "COMMUNITY",  # Support type
}

import bpy
import smtplib
from email.mime.text import MIMEText
from bpy.app.handlers import persistent

# Global variable to track if email has been sent
email_sent = False

# Email Notification Class
class EmailNotification:
    @staticmethod
    @persistent
    def render_complete(scene):
        global email_sent

        if email_sent:
            return

        if not scene.my_checkbox:
            return

        sender_email = scene.sender_email
        receiver_email = scene.receiver_email
        password = scene.email_password

        subject = "Blender Render Complete"
        body = f"Render completed for scene: {scene.name}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)
            print("Email sent!")
        except Exception as e:
            print(f"Error: {e}")

        email_sent = True

    @staticmethod
    def reset_email_flag(scene):
        global email_sent
        email_sent = False

    @staticmethod
    def register():
        bpy.app.handlers.render_complete.clear()
        bpy.app.handlers.render_pre.clear()
        bpy.app.handlers.render_complete.append(EmailNotification.render_complete)
        bpy.app.handlers.render_pre.append(EmailNotification.reset_email_flag)

    @staticmethod
    def unregister():
        bpy.app.handlers.render_complete.remove(EmailNotification.render_complete)
        bpy.app.handlers.render_pre.remove(EmailNotification.reset_email_flag)

# Main Panel
class _PT_ToggleScript(bpy.types.Panel):
    bl_label = "Render Complete Notification"
    bl_idname = "OBJECT_PT_toggle_script"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.prop(scene, "my_checkbox")
        layout.prop(scene, "sender_email")
        layout.prop(scene, "receiver_email")
        layout.prop(scene, "email_password")

# Register/unregister functions
def register():
    bpy.utils.register_class(_PT_ToggleScript)
    
    bpy.types.Scene.my_checkbox = bpy.props.BoolProperty(
        name="Enable Email Notification",
        description="Toggle to enable/disable the email notification",
        default=True,
        update=update_script_status
    )
    bpy.types.Scene.sender_email = bpy.props.StringProperty(
        name="Sender Email",
        description="Email address to send from",
        default=""
    )
    bpy.types.Scene.receiver_email = bpy.props.StringProperty(
        name="Receiver Email",
        description="Email address to send to",
        default=""
    )
    bpy.types.Scene.email_password = bpy.props.StringProperty(
        name="Email Password",
        description="Password for sender email",
        subtype='PASSWORD',
        default=""
    )

    EmailNotification.register()

def unregister():
    bpy.utils.unregister_class(_PT_ToggleScript)
    del bpy.types.Scene.my_checkbox
    del bpy.types.Scene.sender_email
    del bpy.types.Scene.receiver_email
    del bpy.types.Scene.email_password
    EmailNotification.unregister()

def update_script_status(self, context):
    if self.my_checkbox:
        EmailNotification.register()
    else:
        EmailNotification.unregister()

if __name__ == "__main__":
    register()
