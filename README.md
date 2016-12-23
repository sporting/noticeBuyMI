# noticeBuyMI

## Shell script with ezSendGMail and noticeBuyMI.py to notice
    #小米手環
    BuyPage=http://buy.mi.com/tw/accessories/117

    #小米產品名稱
    Product='小米手環'

    NoticeFile=notice.lst

    #mail to
    MailTo=SOMEONE@gmail.com

    #mail subject
    MailSubject='[Notice]buy.mi.com'

    python noticeBuyMI.py -g $Product -u $BuyPage -o $NoticeFile

    if [ -s $NoticeFile ]; then
      exec < $NoticeFile
      while read line
      do
        msg=$msg$line'\n'
      done

      sm $MailTo $MailSubject $msg'\n'$BuyPage
    fi
