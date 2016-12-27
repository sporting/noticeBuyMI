# noticeBuyMI

## Shell script with ezSendGMail and noticeBuyMI.py to notice
    #!/bin/bash

    #log
    log(){
    echo $(date)":[$1] "$2 $3 $4 $5 $6 $7 $8 $9
    }

    cd /home/nick/git/noticeBuyMI
    mail=/home/nick/shell/sm

    IFS=","

    #小米空氣淨化器
    BuyPage=http://buy.mi.com/tw/accessories/183
    #小米產品名稱
    Products=('"小米空氣淨化器 2 白色"','"小米空氣淨化器濾芯"')

    #for Test
    #=======================================
    #小米手環
    #BuyPage=http://buy.mi.com/tw/accessories/117
    #Products=("小米手環 2","小米手環 2")
    #========================================

    NoticeFile=notice.lst

    #mail to
    MailTo=sportingapp+noticeBuyMI@gmail.com

    #mail subject
    MailSubject='[Notice] buy.mi.com'

    log 'Python arguments.Products' "${Products[*]}"
    log 'Python arguments.BuyPage' "$BuyPage"
    log 'Python arguments.NoticeFile' "$NoticeFile"

    python noticeBuyMI.py -g ${Products[*]} -u "$BuyPage" -o "$NoticeFile"

    #-s NoticeFile size >0 
    if [ -s $NoticeFile ]; then
       exec < $NoticeFile
       while read line
       do
           msg=$msg$line"\n"
       done
       
       log 'Mail execution name' "$mail"
       log 'Mail To' "$MailTo"
       log 'Mail Subject' "$MailSubject"
       log 'Mail Message' "$msg$BuyPage"

       $mail "$MailTo" "$MailSubject" "$msg$BuyPage"
    fi

