import sys
import os

def main():

  import Technot
  from Technot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID
  from . import HOST
  
  from .helpers.Config import Config
  from .helpers.core.logger import logging
  from .helpers.core.helpers import printUser
  from .helpers.core.session import techno
  from .start import killer
  from .utils import (
      chkbot,
      add_bot_to_logger_group,
      hekp,
      install_extrarepo,
      load_plugins,
      setup_bot,
      startupmessage,
      verifyLoggerGroup,
  )
  
  LOGS = logging.getLogger("Technot")
  
  print(Technot.__copyright__)
  print("Licensed under the terms of the " + Technot.__license__)
  
  cmdhr = Config.HANDLER
  
  
  async def extrarepo():
      if Config.EXTRA_REPO:
          await install_extrarepo(
              Config.EXTRA_REPO, Config.EXTRA_REPOBRANCH, "xtraplugins"
          )
  
  if HOST == "github actions" and os.patb.exists("Technot/plugins/memify.py"):
    os.remove("Technot/plugins/memify.py")
  if HOST == "github actions" and os.patb.exists("Technot/helpers/memeifyhelpers.py"):
    os.remove("Technot/helpers/memeifyhelpers.py")
  
  try:
      LOGS.info("Starting Userbot")
      LOGS.info("Trying to log in . . . ")
      techno.loop.run_until_complete(setup_bot())
      async def ptusr():
        bot=await techno.get_me()
        printUser(bot)
      techno.loop.run_until_complete(ptusr())
      LOGS.info("TG Bot Startup Completed")
  except Exception as e:
      LOGS.error(f"{e}")
      sys.exit()
  
  
  async def startup_process():
      try:
          await verifyLoggerGroup()
          await load_plugins("plugins")
          await load_plugins("assistant")
          if os.path.exists("Technot/extplugins"):
            load_plugins("extplugins")
          await killer()
          print("----------------")
          print("Starting Bot Mode!")
          print("⚜ Technot Has Been Deployed Successfully ⚜")
          print("OWNER - @Technoboy_02")
          print("Group - @Technot_Official")
          print("----------------")
          await verifyLoggerGroup()
          await add_bot_to_logger_group(BOTLOG_CHATID)
          if PM_LOGGER_GROUP_ID != -100:
              await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
          await startupmessage()
          await extrarepo()
          await hekp()
      except Exception as e:
          LOGS.error(f"{str(e)}")
          sys.exit()
  
  
  techno.loop.run_until_complete(startup_process())
  
  if len(sys.argv) not in (1, 3, 4):
      techno.disconnect()
  else:
      try:
          techno.run_until_disconnected()
      except ConnectionError:
          pass


if __name__=="__main__":
  main()