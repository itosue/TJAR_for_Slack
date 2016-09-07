# -*- coding: utf-8 -*-
import bpy
from bpy.app.handlers import persistent
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty
import json
import urllib.request

bl_info = {
    "name": "throw json after rendering for Slack",
    "author": "itosue",
    "version": (1, 1),
    "blender": (2, 77, 0),
    "location": "Properties > Render",
    "description": "This addon sends message to Slack after rendering.",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "https://github.com/itosue/TJAR_for_Slack/issues",
    "category": "Render"
}

class tjafAddonPreferences(AddonPreferences):
    bl_idname = __name__
    
    URL = StringProperty(
        name="Webhook URL",
        default="https://hooks.slack.com/services/XXXX/YYYY/ZZZZZZ",
        )
    cn_name = StringProperty(
        name="Channel",
        default="#general",
        )

# May be implement later
#    message = StringProperty(
#            name="Message",
#            default="render finished",
#        )
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Please set your WebhookURL and Channel")
        layout.prop(self, "URL")
        layout.prop(self, "cn_name")
#        layout.prop(self, "message") # May be implement later

        
class ObjectCheckPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_check"
    bl_label = "Throw JSON After Rendering"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}

    bpy.types.Scene.MyBool = BoolProperty(
        name = "send notification",
        default = True,
        description = "Check to send notification.")
    
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        layout.prop(scn, 'MyBool')
        
        
def throw_json(scene,message):
    if scene.MyBool :
        print("trying to send message \"" + message +"\"...")
        user_preferences = bpy.context.user_preferences    
        addon_prefs = user_preferences.addons[__name__].preferences
        slackURL = addon_prefs.URL
        payload = {
            "channel" : addon_prefs.cn_name,
            #"text" : addon_prefs.message, # May be implement later.
            "text" : message,
            "username" : "blender",
            "icon_emoji" : "ghost"
        }
        encoded_data = json.dumps(payload).encode('utf8')
        req = urllib.request.Request(slackURL,data=encoded_data,headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(req)
        print("message sent. response is \"" + response.read().decode('utf8') + "\"")
        return {'FINISHED'}
    else:
        print("sending notification is disabled")
        return {'FINISHED'}

def render_canceled(scene):
    throw_json(scene,"render canceled")
    
def render_finished(scene):
    throw_json(scene,"render completed")

def register():
    bpy.utils.register_class(tjafAddonPreferences)
    bpy.utils.register_class(ObjectCheckPanel)
    bpy.app.handlers.render_cancel.append(render_canceled)
    bpy.app.handlers.render_complete.append(render_finished)

def unregister():
    bpy.utils.unregister_class(tjafAddonPreferences)
    bpy.utils.unregister_class(ObjectCheckPanel)
    bpy.app.handlers.render_cancel.remove(render_canceled)
    bpy.app.handlers.render_complete.remove(render_finished)

if __name__ == "__main__":
    register()
