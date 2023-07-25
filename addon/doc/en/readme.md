# Everything

* Author: Nael Sayegh
* URL: [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* Download the [stable version][1] ;
<!-- * Download the [Latest version on Nael-AccessVision.com](https://) ; -->
* NVDA Compatibility: 2021.3 and above ;
* [Source code on GitHub][2] ;

# Description

This extension adds the ability to change the position of column information announced by NVDA in Everything, such as modification date, size, or path, as well as the ability to enable or disable the announcement of column names.

## How it works

Once this extension is installed, the default announcement of columns is as follows: name, date, size, path.
To modify this order, use the shortcut ctrl+shift+O.
A file will open, and to change the order, scroll down to the line starting with lines =
After the equal sign, you can move the variables to change the order in which the columns appear.
Make sure to leave a space between each variable when modifying them.
By default, the announcement of columns is enabled. If you want to disable it, scroll down in the file to the line sayColumn=True.
To disable it, write False after the equal sign.
If you want to re-enable it, write the number True after the equal sign.
Please note that the capitalization is important when changing this value.
Once you are done, save the modifications and close the file.
To apply the changes, use the shortcut ctrl+shift+r in Everything.

## Changes

### Version 2023.07.16
  * First version

Copyright ©: 2023 (Nael Sayegh and Nael-AccessVision)

<!-- links section -->

[1]: https://github.com/Nael-Sayegh/Everything/releases/download/2023.07.24/everything-2023.07.24.nvda-addon

[2]: https://github.com/Nael-Sayegh/Everything
