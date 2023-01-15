# Cheat Table Hierarchy Dumper

A command-line tool for dumping the hierarchical structure of a cheat table.

Note: You need to specify the path to your Cheat Table in the code.

<pre>
SCRIPTS ▼
├─ INTERFACE ▼
│   ├─ Teammate health hud 2.1
│   │   ├─ Enable health display
│   │   ├─ Color management
│   │   ├─ Color reset on map load
│   │   ├─ Kill counter color fix
│   │   ├─ Incoming damage indicator color fix
│   │   └─ Debug ▼
│   │       ├─ target
│   │       ├─ get target health
│   │       │   ├─ target health
│   │       │   ├─ target max health
│   │       │   └─ target_class
│   │       ├─ current_icon_color
│   │       ├─ current_icon_color_addr
│   │       └─ current_background_color_addr
│   ├─ Hide interface (CTRL + H)
│   ├─ Show player position
│   │   ├─ String format
│   │   └─ Show camera position instead
│   │       └─ String format
│   ├─ Override camera position
│   │   ├─ x
│   │   ├─ y
│   │   └─ z
│   ├─ Enable chat in singleplayer
│   │   ├─ Chat input fix
│   │   └─ Enable TAB key support
│   ├─ Disable crosshair fade
│   └─ misc ▼
│       ├─ Enable alternative crosshairs
│       ├─ Disable crosshair color switch
│       ├─ Make objects on the minimap more visible (map reload)
│       ├─ Hide spawn select UI (has effect on menus)
│       └─ Enable reload display for all weapons
├─ MATCH ▼
│   ├─ Disable ticket draining (kills)
│   ├─ Disable ticket draining (outnumbered)
│   ├─ Disable CP discapturing
│   ├─ Disable AI
│   ├─ Get target info ▼
│   │   ├─ target health
│   │   ├─ target max health
│   │   ├─ target_class (does not work for all)
│   │   ├─ target_weapon (disabled in script)
│   │   └─ Position
│   │       ├─ X
│   │       ├─ Y
│   │       ├─ Z
│   │       └─ Teleport into target
│   └─ Get speed values ▼
│       ├─ Acceleration
│       ├─ Max speed
│       ├─ Max strafe speed
│       └─ Max turn speed
├─ TELEPORTS ▼
│   └─ Get target coords (shoot bullet)
│       ├─ Teleport to bullet coords (Hotkey: ^)
│       ├─ Bullet X
│       ├─ Bullet Y
│       └─ Bullet Z
├─ RENDERING ▼
│   ├─ Render max-height grid
│   ├─ Render map boundaries
│   ├─ Turn off holos
│   ├─ Wireframe shadows
│   ├─ Beyblade mode
│   └─ Render weird object border boxes
├─ PROFILE ▼
│   ├─ Disable profile integrity check
│   └─ Enable Jub Jub easteregg for any profile/name
├─ CHEATS ▼
│   ├─ Godmode
│   ├─ Infinite Jetpack for all
│   ├─ Infinite ammo
│   │   ├─ Infinite ammo (2)
│   │   └─ Infinite ammo (3)
│   ├─ Disable overheat
│   ├─ Disable spread
│   ├─ Rapidfire
│   │   └─ Rapidfire (2)
│   ├─ Unit speedhack
│   ├─ NoClip Hotkey (hold shift)
│   │   └─ No clip
│   ├─ Disable negative kills
│   ├─ Disable Leaving Battlefield
│   └─ [WIP] One shot kill enemies
└─ misc ▼
    ├─ Nuke all 💀
    ├─ Disable AI from using automatic rifles... ?
    ├─ Disable HEALTH powerups
    ├─ Disable Jabba's trapdoor
    └─ Get selected command post ID
        └─ CP ID
</pre>
