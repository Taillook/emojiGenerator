emojiGenerator
====

![Open issues](https://img.shields.io/github/issues/Taillook/emojiGenerator.svg)
![Closed issues](https://img.shields.io/github/issues-closed/Taillook/emojiGenerator.svg)
![MIT licensed](https://img.shields.io/github/license/mashape/apistatus.svg)  
Emoji generation script for "Slack".

## Description
Slack can set custom Emoji.  
In this project, we develop scripts for generating emoji using string.

***DEMO:***  
`python generate_emoji.py JapaneseStrings(max length 4) --font /path/to/font.ttf`  
![にほんご](http://i.imgur.com/gizAfKB.png)

## This project VS. Emoji-Web
This script can cleate Emoji at console.  
Emoji-Web is intuitive, but we don't want to use a mouse.

## Requirement

- Python 3.5
- PIL

## Usage
`python generate_emoji.py JapaneseStrings(max length 4) options`

### Options
```
--font /path/to/font.ttf
--color '#000000'
```

## Installation
We planning to use pip.  
```
git clone https://github.com/Taillook/emojiGenerator.git
```

## Futures
- FontSize auto resize

## Contribution
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Licence

[MIT](https://github.com/Taillook/emojiGenerator/blob/master/LICENSE)

## Author

Twitter: [@Taillook](https://twitter.com/Taillook)  
email: taillook.s@gmail.com
