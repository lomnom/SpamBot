which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

brew list python3 || brew install python3 #install python3

if python3 -c "import pyautogui" &> /dev/null; then
    echo 'all good'
else
    echo 'still needs pyautogui!'
    pip3 install pyautogui
fi
python3 spam.py
