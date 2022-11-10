# gt-dotfiles

sudo apt -y install stow

stow -v -t ~/.emacs.d ~/git/gt-dotfiles/emacs

stow -v -R -t ~/.emacs.d -d ~/git/gt-dotfiles emacs  


## Python IDE Notes
### Static type checker for Python
https://www.npmjs.com/package/pyright  
https://github.com/microsoft/pyright/blob/main/docs/configuration.md  
sudo pip3 install pyright
or
sudo npm install -g pyright

### Flake8, Jedi, etc.

https://steelkiwi.com/blog/emacs-configuration-working-python/  

https://github.com/paetzke/py-autopep8.el  
https://pypi.org/project/flake8/  
https://flake8.pycqa.org/en/latest/index.html#quickstart  

``` shell
sudo pip3 install flake8
```
https://www.reddit.com/r/emacs/comments/evmjbh/flake8/  
https://blog.ironboundsoftware.com/2016/12/05/improving-your-python-pylint-and-flake8-emacs/  
https://www.flycheck.org/en/27/_downloads/flycheck.html  
https://www.reddit.com/r/emacs/comments/wa7iwz/lsp_with_pyright_and_flake8/ # IMPORTANT

### lsp-mode
https://ianyepan.github.io/posts/emacs-ide/  



## General
https://sachachua.com/dotemacs/index.html#babel-init  
https://gist.github.com/widdowquinn/987164746810f4e8b88402628b387d39  
https://gitlab.com/skybert/my-little-friends/-/blob/master/emacs/.emacs#L1472  
https://www.fullstackpython.com/emacs.html  


### Elisp
http://xahlee.info/emacs/emacs/elisp_datetime.html  
https://www.gnu.org/software/emacs/manual/html_node/elisp/Accessing-Variables.html  
https://wikemacs.org/wiki/Emacs_Lisp_Cheat_Sheet  

### Themes
https://emacsthemes.com/  
https://github.com/myTerminal/theme-looper  

### use-package
https://ianyepan.github.io/posts/setting-up-use-package/#:~:text=Setting%20use%2Dpackage%2Dalways%2D,the%20missing%20ones%20for%20you.  
https://github.com/jwiegley/use-package  
https://jwiegley.github.io/use-package/keywords/  
http://cachestocaches.com/2015/8/getting-started-use-package/  
https://github.com/jwiegley/use-package/blob/master/README.md#key-binding  
https://emacs.stackexchange.com/questions/39121/use-package-init-or-config  
https://www.masteringemacs.org/article/spotlight-use-package-a-declarative-configuration-tool#:~:text=Each%20type%20works%20in%20a%20slightly%20different%20way.&text=The%20%3Aconfig%20keyword%20executes%20the,like%20function%20and%20symbol%20declarations.  


### Org-Mode
http://cachestocaches.com/2016/9/my-workflow-org-agenda/  

### Projectile
http://tuhdo.github.io/helm-projectile.html  

### Yasnippet
https://www.emacswiki.org/emacs/Yasnippet  


### Markdown Live
https://github.com/defunkt/markdown-mode  
https://github.com/shime/emacs-livedown  


### Git
https://magit.vc/  
https://emacsair.me/2017/09/01/magit-walk-through/  

### Neo Tree
https://www.emacswiki.org/emacs/NeoTree  
https://github.com/jaypei/emacs-neotree  

### Themes
https://emacsthemes.com/popular/index.html  
M-x package-install
M-x load-theme
https://github.com/toroidal-code/cycle-themes.el  

### Reading List
https://steelkiwi.com/blog/emacs-configuration-working-python/  



