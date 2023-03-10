import asyncio

from .. import techno
from ..helpers.core.logger import logging
from ..helpers.core.managers import eor
from . import mention

menu_category = "useless"

LOGS = logging.getLogger(__name__)
from . import eor, techno

menu_category = "fun"


@techno.techno_cmd(
    pattern="gim$",
    command=("gim", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}gim",
    },
)
async def gim(event):
    "Fun animation try yourself to know more"
    a = "π±ββββββπ±\nπ        \         /          π\nβ­          \π/            β­\nβ¨           π½             β¨\n              /    \ \n            π    π"
    await event.edit(a)


@techno.techno_cmd(
    pattern="holi$",
    command=("holi", menu_category),
    info={
        "header": "Wish Happy Holi",
        "usage": "{tr}holi",
    },
)
async def holi(event):
    "Wish Holi"
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit("π»πΆππππ»πππΎ")
    animation_chars = [
        "[Happy Holy Once Again To All](https://telegra.ph/file/ee2a7df3bc0a3334194b0.jpg)",
        "[Β­](https://telegra.ph/file/2e4ca1bc7f747858fe98d.jpg)",
        "[γ€Β­](https://telegra.ph/file/7f842a8f3aba51b8d5ac7.jpg)",
        "[Β­γ€](https://telegra.ph/file/f24efadcd212d996bb937.jpg)",
        "[γ€](https://telegra.ph/file/97b713907cd99f6831932.jpg)",
        "[π¨](https://telegra.ph/file/0b604517d37fc519f16b6.jpg)",
        "[β£οΈ](https://telegra.ph/file/aaadc0e87f78be44cfdaa.jpg)",
        "[β£οΈπ¨γ€Β­](https://telegra.ph/file/d7d62ebbff4b5b092d4e0.jpg)",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@techno.techno_cmd(
    pattern="cry$",
    command=("cry", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}cry",
    },
)
async def cry(event):
    "Fun animation try yourself to know more"
    animation_interval = 1

    animation_ttl = range(0, 35)

    await event.edit("crying")

    animation_chars = [
        ";__",
        ";___",
        ";____",
        ";_____",
        ";______",
        ";_______",
        ";________",
        ";__________",
        ";____________",
        ";______________",
        ";________________",
        ";__________________",
        ";____________________",
        ";______________________",
        ";________________________",
        ";_________________________",
        ";_________________________",
        ";________________________",
        ";_______________________",
        ";______________________",
        ";_____________________",
        ";____________________",
        ";___________________",
        ";__________________",
        ";_________________",
        ";________________",
        ";_______________",
        ";_____________",
        ";___________",
        ";_________",
        ";_______",
        ";_____",
        ";____",
        ";___",
        ";__",
        ";You made me `CRY`",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@techno.techno_cmd(
    pattern="unoob$",
    command=("unoob", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}unoob",
    },
)
async def unoob(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(9)
    event = await eor(event, "unnoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "YoU",
        "aRriVe",
        "π",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe π",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@techno.techno_cmd(
    pattern="menoob$",
    command=("menoob", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}menoob",
    },
)
async def menoob(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(9)
    event = await eor(event, "menoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "i",
        "aRriVe",
        "π",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe π",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@techno.techno_cmd(
    pattern="upro$",
    command=("upro", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}upro",
    },
)
async def upro(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(8)
    event = await eor(event, "upro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "YoU",
        "aRriVe",
        "π",
        "EvErYbOdY iZ PeRu uNtiL YoU aRriVe π",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@techno.techno_cmd(
    pattern="mepro$",
    command=("mepro", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}mepro",
    },
)
async def mepro(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(8)
    event = await eor(event, "mepro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "i",
        "aRriVe",
        "π",
        "EvErYbOdY iZ PeRu uNtiL i aRriVe π",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@techno.techno_cmd(
    pattern="quickheal$",
    command=("quickheal", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}quickheal",
    },
)
async def quickheal(event):
    "animation command"
    animation_interval = 5
    animation_ttl = range(11)
    event = await eor(event, "quickheal")
    animation_chars = [
        "`Downloading File..`",
        "`File Downloaded....`",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult: No Virus Found...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@techno.techno_cmd(
    pattern="sqh$",
    command=("sqh", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}sqh",
    },
)
async def sqh(event):
    "animation command"
    animation_interval = 0.1
    animation_ttl = range(11)
    event = await eor(event, "sqh")
    animation_chars = [
        "`Downloading File..`",
        "`File Downloaded....`",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult: No Virus Found...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@techno.techno_cmd(
    pattern="vquickheal$",
    command=("vquickheal", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}vquickheal",
    },
)
async def vquickheal(event):
    "animation command"
    animation_interval = 5
    animation_ttl = range(11)
    event = await eor(event, "vquickheal")
    animation_chars = [
        "`Downloading File..`",
        "`File Downloaded....`",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\nβββββββββββββββββββββββββ `",
        "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult:β οΈVirus Foundβ οΈ\nMore Info: Torzan, Spyware, Adware`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@techno.techno_cmd(
    pattern="macoc$",
    command=("macoc", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}macoc",
    },
)
async def macoc(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await eor(event, "macos")
    animation_chars = [
        "`Connecting To Hackintosh...`",
        "`Initiating Hackintosh Login.`",
        "`Loading Hackintosh... 0%\nβββββββββββββββββββββββββ `",
        "`Loading Hackintosh... 3%\nβββββββββββββββββββββββββ `",
        "`Loading Hackintosh... 9%\nβββββββββββββββββββββββββ `",
        "`Loading Hackintosh... 23%\nβββββββββββββββββββββββββ `",
        "`Loading Hackintosh... 39%\nβββββββββββββββββββββββββ `",
        "`Loading Hackintosh... 69%\nβββββββββββββββββββββββββ `",
        "`Loading Hackintosh... 89%\nβββββββββββββββββββββββββ `",
        "`Loading Hackintosh... 100%\nβββββββββββββββββββββββββ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Hackintosh`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@techno.techno_cmd(
    pattern="windows$",
    command=("windows", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}windows",
    },
)
async def windows(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await eor(event, "windows")
    animation_chars = [
        "`Connecting To Windows 10...`",
        "`Initiating Windows 10 Login.`",
        "`Loading Windows 10... 0%\nβββββββββββββββββββββββββ `",
        "`Loading Windows 10... 3%\nβββββββββββββββββββββββββ `",
        "`Loading Windows 10... 9%\nβββββββββββββββββββββββββ `",
        "`Loading Windows 10... 23%\nβββββββββββββββββββββββββ `",
        "`Loading Windows 10... 39%\nβββββββββββββββββββββββββ `",
        "`Loading Windows 10... 69%\nβββββββββββββββββββββββββ `",
        "`Loading Windows 10... 89%\nβββββββββββββββββββββββββ `",
        "`Loading Windows 10... 100%\nβββββββββββββββββββββββββ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10`\n\n**My PC Specs:**\n\n **CPU:** __3.4GHz ryzen 9 5950x (16-core,32 threads 64MB cache, up to 4.9GHz)__\n\n**Graphics:** __Nvidia GeForce RTX 3090 OC (24GB GDDR6X)__\n\n**RAM:** __64GB DDR4 (4000MHz)__\n\n**Screen:** __17.3-inch, UHD (3840 x 2160) 144Hz Hdr G-Sync__\n\n**Storage:** __512GB nvme gen 4 SSD, 5 TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.1, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), 2 HDMI2.0, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@techno.techno_cmd(
    pattern="linux$",
    command=("linux", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}linux",
    },
)
async def linux(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await eor(event, "linux")
    animation_chars = [
        "`Connecting To Linux...`",
        "`Initiating Linux Login.`",
        "`Loading Linux... 0%\nβββββββββββββββββββββββββ `",
        "`Loading Linux... 3%\nβββββββββββββββββββββββββ `",
        "`Loading Linux... 9%\nβββββββββββββββββββββββββ `",
        "`Loading Linux... 23%\nβββββββββββββββββββββββββ `",
        "`Loading Linux... 39%\nβββββββββββββββββββββββββ `",
        "`Loading Linux... 69%\nβββββββββββββββββββββββββ `",
        "`Loading Linux... 89%\nβββββββββββββββββββββββββ `",
        "`Loading Linux... 100%\nβββββββββββββββββββββββββ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Linux`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@techno.techno_cmd(
    pattern="stock$",
    command=("stock", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}stock",
    },
)
async def stock(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await eor(event, "stock")
    animation_chars = [
        "`Connecting To Symbian OS...`",
        "`Initiating Symbian OS Login.`",
        "`Loading Symbian OS... 0%\nβββββββββββββββββββββββββ `",
        "`Loading Symbian OS... 3%\nβββββββββββββββββββββββββ `",
        "`Loading Symbian OS... 9%\nβββββββββββββββββββββββββ `",
        "`Loading Symbian OS... 23%\nβββββββββββββββββββββββββ `",
        "`Loading Symbian OS... 39%\nβββββββββββββββββββββββββ `",
        "`Loading Symbian OS... 69%\nβββββββββββββββββββββββββ `",
        "`Loading Symbian OS... 89%\nβββββββββββββββββββββββββ `",
        "`Loading Symbian OS... 100%\nβββββββββββββββββββββββββ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Symbian OS`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@techno.techno_cmd(
    pattern="os$",
    command=("os", menu_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}os",
    },
)
async def os(event):
    "animation command"
    animation_interval = 0.1
    animation_ttl = range(7)
    event = await eor(event, "os")
    animation_chars = [
        "`Scanning OS...`",
        "`Scanning OS......`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβοΈ `.macos`\nβοΈ `.windows`\nβοΈ `.linux`\nβοΈ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.macos`\nβοΈ `.windows`\nβοΈ `.linux`\nβοΈ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.macos`\nβ `.windows`\nβοΈ `.linux`\nβοΈ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.macos`\nβ `.windows`\nβ `.linux`\nβοΈ `.stock`",
        "__Current Loaded OS: Symbian OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.macos`\nβ `.windows`\nβ `.linux`\nβ `.stock`\n\nDeveloped By: @Technoboy_02",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])


@techno.techno_cmd(
    pattern="independence(?:\s|$)([\s\S]*)",
    command=("independence", menu_category),
    info={
        "header": "Wish Happy Independence Day",
        "description": "It Can Help U To Send Independence Day Message ",
        "usage": [
            "{tr}independence",
        ],
    },
)
async def independence(event):
    "Wish Happy Independence Day"
    animation_interval = 6
    animation_ttl = range(0, 17)
    await event.edit("Starting...")
    animation_chars = [
        "**Π½ΡββΞΏ!π**",
        "**Π½ΞΏΟ Ξ±ΡΡ Ο?**",
        f"**{mention} : Π½Ξ±ΟΟΞ³ ΞΉΠΈβΡΟΡΠΈβΡΠΈΟ²Ρ βΞ±Ξ³**",
        "ΟΞΉΡΠ½ΞΉΠΈg Ο Π½Ξ±ΟΟΞ³ ΞΉΠΈβΡΟΡΠΈβΡΠΈΟ²Ρ βΞ±Ξ³",
        "**Happy π Indpendence Day!**",
        "**From every mountain side Let Fredom Ring**",
        "**Independence means.. enjoying freedom and empowering others too to let them do so.**",
        "Ν²Ο΄α αͺα½ αα¬ αͺα‘α¬ ?α‘α¬α¬ α΄α¬ααͺα?Υα¬ α·αͺΞα½ Υαͺαα‘α?ααα¬α  Ν²α»α¬α‘α¬ αααα¬Υ ?Ο΄α‘ αΞα ααͺ \nΥαͺαα?Ν²α¬ Ν²α»α¬ αα‘α¬αͺΝ² ΥΟ΄α?αΥ",
        "[ΖΞΏΡ Ο](https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg)",
        "[Π½Ξ±ΟΟΞ³ ΞΉΠΈβΟΡΠΈβΡΠΈΟ²Ρ βΞ±Ξ³](https://t.me/Techno_Userbot)",
    ]
    for i in animation_ttl:  # By @Technoboy_02 Technot

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17], link_preview=True)
