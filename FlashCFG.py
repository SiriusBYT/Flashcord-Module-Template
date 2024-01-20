"""
This tool lets you quickly configure your page in a hurry.
Read https://github.com/SiriusBYT/Flashcord/wiki/The-Flashcord-Store-Template for how this file works.

This script does not do the following but will in the future:
- Set "Other Modules by X" embeds automatically (A long time later! Requires internet & communication to sirio-network.com)
"""

# Edit the following things
IsRepluggedPlugin = False
IsRepluggedTheme = False # TBD, does absolutely nothing for now

Name = "FlashCFG-built Store Template"
Short_Description = "This store page was created using the Flashcord Store Quick Config Python Script!"
Version = "v1.1.0"
License_Year = "2024"
License = "Unlicense"


GitHub_Profile = "SiriusBYT" # Notice: this will be converted to lowercase and will be your folder name after modules/plugins
GitHub_Repo = "Flashcord-Store-Template" 
GitHub_Contributors = "SiriusBYT"

Discord = "https://discord.gg/z93kHwGuZt"
SNDL_Theme = "Light"
Embed_Color = "#FF69FF"

Store_Page_Name = "module_template.html" # NO capitals! Underscores only! CANNOT HAVE "-files" AT THE END!
Folder_Name = "module_template-files" # NO capitals! Underscores only! Must have "-files" at the end!
Embed_FileName = "embed-banner.png" # Notice: GIFs work!
Store_Embed_FileName = "embed-banner.png" # I would still suggest against it due to AuraCloud-E2A's limited space.

Long_Description = '<p>Long descriptions are actually quite the doozy, they require actual HTML code to be set inside this little variable. \
While quite impractical looking, it lets you entirely skip the manual process of opening your Store Page ENTIRELY!</p> \
<p class="SNDL-ParenthesizedText">This has limitations though... Of course...</p> \
<p>You obviously need HTML and SNDL knowledge if you wanna make this look as nice as possible.</p> \
<p>But of course since this is just a python variable inserted into HTML code that means that yes, you can:</p> \
<div class="SNDL-DashList"> \
    <p>Create certain parts of your long description to have parts of your module/plugin info update itself when you rebuild your Store page! For example this is version ' + Version + ' of FlashCFG that built this page!</p> \
    <p>And you can probably do a lot more but since I ran out of ideas, well you go figure it out yourself.</p> \
</div>'

# NOT recommended to modify, do this only if you know what you're doing! 
StoreTemplate = "flashcord/store/templates/default/default_template.html"

# Don't touch this, it will get overwritten anyways but still. Don't touch just in case.
HTMLFile = ""

# Don't touch this either. This will cause problems if your store page is for a Flashcord Module!
UserFolderName = GitHub_Profile.lower()

# This code is disgusting but it works, will optimize when I feel like it.
# NOTICE: this has ZERO error handling (or very little)! This is fucking horrible but I don't know yet how to do those and at the time of writing it's fucking 23h28
def GetHTMLFile(FileConcerned):
    if FileConcerned == "Store Page":
        if IsRepluggedPlugin == True:
            File = "flashcord/store/plugins/" + GitHub_Profile.lower() + "/" + Store_Page_Name
        else:
            File = "flashcord/store/modules/" + GitHub_Profile.lower() + "/" + Store_Page_Name
    elif FileConcerned == "Embed":
        if IsRepluggedPlugin == True:
            File = "flashcord/store/plugins/" + GitHub_Profile.lower() + "/" + Folder_Name + "/embed.html"
        else:
            File = "flashcord/store/modules/" + GitHub_Profile.lower() + "/" + Folder_Name + "/embed.html"
    else:
        print('[FlashCFG // GetHTMLFile] ERROR: Sirius A was here and pissed on the moon. (What the fuck is a "', FileConcerned, '"?!)')
        return "FUCK"
    return File

def FileBackup(FileToBackup):
    print("[FlashCFG // Backup] The", FileToBackup, "will now be backed up...")
    HTMLFile = GetHTMLFile(FileToBackup)
    HTMLFile_Backup = HTMLFile.replace(".html",".bak-html")
    with open(HTMLFile, 'r', encoding='utf-8') as HTMLFile_File:
        with open(HTMLFile_Backup, 'w', encoding='utf-8') as HTMLFile_Backup_File:
            HTMLFile_Backup_File.write((HTMLFile_File.read()))
    print("[FlashCFG // Backup] ", HTMLFile_Backup, "has been created and is now backed up.")

def HTMLConfigurator(Step):
    # We're doing this the MarkSNDL way, I can't fucking figure out how to do this the objectively better way
    # This is surprisingly way better than the current version of MarkSNDL though LMFAO
    HTMLArray = []
    if Step == 0:
        print("[FlashCFG // HTML-CFG] Now building the Store Page...")
        HTMLFile = GetHTMLFile("Store Page")
        StepFile = "// Store Page"
    elif Step == 1:
        print("[FlashCFG // HTML-CFG] Now building the Embed...")
        HTMLFile = GetHTMLFile("Embed")
        StepFile = "// Embed"
    else:
        print("[FlashCFG // Backup] WARNING: Sirius A was here and replaced Sirius B's Yae wallpaper with a Kirara one.", '(What the fuck is Step "', Step, '"?!)')
        return "FUCK"

    with open(StoreTemplate, 'r', encoding='utf-8') as StoreTemplate_File:
        with open(HTMLFile, 'w', encoding='utf-8') as EditHTML_File:
            EditHTML_File.write("")
        with open(HTMLFile, 'a', encoding='utf-8') as EditHTML_File:
            HTMLArray = StoreTemplate_File.readlines()
            for line in range (len(HTMLArray)):
                # print('[FlashCGG] Processing Line"', line, '" which is "', HTMLArray[line], '".')
                HTMLArray[line] = HTMLArray[line].replace("[NAME]", Name)
                HTMLArray[line] = HTMLArray[line].replace("[SHORT_DESC]", Short_Description)
                HTMLArray[line] = HTMLArray[line].replace("[LONG_DESC]", Short_Description)
                HTMLArray[line] = HTMLArray[line].replace("[VERSION]", Version)
                HTMLArray[line] = HTMLArray[line].replace("[LICENSE_YEAR]", License_Year)
                HTMLArray[line] = HTMLArray[line].replace("[LICENSE]", License)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_PROFILE]", GitHub_Profile)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_REPO]", GitHub_Repo)
                HTMLArray[line] = HTMLArray[line].replace("[GITHUB_CONTRIBUTORS]", GitHub_Contributors)
                HTMLArray[line] = HTMLArray[line].replace("[DISCORD_LINK]", Discord)
                HTMLArray[line] = HTMLArray[line].replace("[THEME]", SNDL_Theme)
                HTMLArray[line] = HTMLArray[line].replace("[EMBED_COLOR]", Embed_Color)
                HTMLArray[line] = HTMLArray[line].replace("[STORE_PAGE_NAME]", Store_Page_Name)
                HTMLArray[line] = HTMLArray[line].replace("[FOLDER_NAME]", Folder_Name)
                HTMLArray[line] = HTMLArray[line].replace("[EMBED_FILENAME]", Embed_FileName)
                HTMLArray[line] = HTMLArray[line].replace("[STORE_EMBED_FILENAME]", Store_Embed_FileName)
                HTMLArray[line] = HTMLArray[line].replace("[STORE_USER_FOLDER]", UserFolderName)
                EditHTML_File.write(HTMLArray[line])
                ProcessingProgress = (line/len(HTMLArray))*100
                print('[FlashCFG // HTML-CFG] Proccessed Line', line, '/', len(HTMLArray), '(', ProcessingProgress, '%).', StepFile)
                # print('[FlashCGG] Processed Line is now "', HTMLArray[line], '".')

def FlashcordStoreConfig():
    print("[FlashCFG] Script initiated.")
    FileBackup("Store Page")
    HTMLConfigurator(0)
    FileBackup("Embed")
    HTMLConfigurator(1)
    print("[FlashCFG] Script complete.")
    return

FlashcordStoreConfig()