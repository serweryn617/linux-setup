# Polish Workman Keyboard Layout for Xorg

Add new layout:
```
sudo cp wm /usr/share/X11/xkb/symbols/wm
```

Add this line under `! layout` in `/usr/share/X11/xkb/rules/evdev.lst`:
```
  wm              Polish Workman
```

Add new layout in `<layoutList>` section in `/usr/share/X11/xkb/rules/evdev.xml`:
```xml
    <layout>
      <configItem>
        <name>wm</name>
        <!-- Keyboard indicator for Polish Workman layouts -->
        <shortDescription>wm</shortDescription>
        <description>Polish Workman</description>
        <countryList>
          <iso3166Id>PL</iso3166Id>
        </countryList>
        <languageList>
          <iso639Id>pol</iso639Id>
        </languageList>
      </configItem>
    </layout>
```

