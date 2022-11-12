from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
import os
import csv
import re

import requests
from bs4 import BeautifulSoup

from twocaptcha import TwoCaptcha

a = """<head id="head"><meta http-equiv="content-type" content="text/html; charset=utf-8"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="-1"><link rel="stylesheet" href="../css/base.css" type="text/css" media="screen, projection, tv"><link rel="stylesheet" href="../css/print.css" type="text/css" media="print"><link rel="stylesheet" href="https://code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">

    <!-- Add fancyBox -->
    <link rel="stylesheet" href="../css/fancybox/jquery.fancybox.css?v=2.1.5" type="text/css" media="screen"><link id="Link1" rel="stylesheet" href="../css/facr-icons.css" type="text/css" media="screen, projection, tv"><link rel="stylesheet" href="../css/facr.css" type="text/css" media="screen, projection, tv"><link rel="stylesheet" href="../css/medium.css" media="screen, projection, tv"><link href="../favicon.ico" rel="shortcut icon" type="image/ico">

    <script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript">
        var messageInfo = { show: false, title: 'Upozornění', msg: '', type: '' };
        var messageEval = null;
        var boxLocalSelected = null;


        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date(); a = s.createElement(o),
        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

        ga('create', 'UA-38697170-2', 'fotbal.cz');
        ga('send', 'pageview');
        
        function setHeartbeat() {
            setTimeout("heartbeat()", 300000); // every 5 min
        }
        function heartbeat() {
            $.ajax({
                url: facrConfig.rootUrl + 'refresh-state.aspx',
            }).done(function (data) {
                setHeartbeat();
            });
        }
       
    </script>
<title>
	IS FAČR
</title><style type="text/css">.fancybox-margin{margin-right:17px;}</style></head>
<body class="admin has-js">
    <form method="post" action="./detail-souteze.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6&amp;fbclid=IwAR3NizZ2RB1Ffj8fObluwhR9wlFEeCYRB7ihXm8mCwy308cDMMzQMfMKuaU" id="Form1">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="">
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="">
<input type="hidden" name="__LASTFOCUS" id="__LASTFOCUS" value="">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="m8M3k7acXJtvGXyAmtHxgN/jbMRcqtD2wEwCSm9W4TBpvm9FaZkRYsj6lNtRPLIRH6HDPq0s4+1xJl88hcVuOunAQR0qq4J3p0dzx1NjvXIEfeCdrAKiK22l+EETNqp+plqpUfKFzM18jwO8YjzNuzjQuMgVyDx6eDiY4UITgN3KbOREhDzOO1Dm1gFYCsoMjQkJ1pAhP5SBklvc4+BcbWYxqJNbjoW5QFA/XajCq3rZafYo0M3bfeL/XIeUieAbwm13qWIcHXiqaM1QpRxOcxQYh2ES6454Prejlit4CFCcaI4sTUGBu1gyj1yO3P1yV/djQUxqxmIaE7/wvP30fIfVEB/JmpAff+P/9ELTfGRrAGfGKkLtPx9l20aOQmltDdSC8DpMPl2yxkuECm2BrbeRsRjTRwcelu07KMQ2OFZZCktf5yY4ncphNssB+XhD3gef0m18WUNCfFmTtYe65ts10d1TgPhEse23esknc7sUmF0oUV22boMKNB3Ebvh1OvabUZzDXvBuF3f7nOFRYDNdZC9Q5UgvX3FtGVyK808BeO2WgftErtxFQNS9rs8ibzFFZgCCSfcFD6oiek9BSvZ/JUHCc4lDBDIRWyRekSO5h71eR/rlrhiPr9Z+WUbhfhHHEQI3f0kzxTj+FOVWsFF1cp2uhHA9sKY5AclCQJQSaSGQf7PDcJbYLooU3z7/tGetm8tnoDgO7abNyXvOcoXrfkY+F7LXnU45eWCiLyW+GMzDUYEWoOuiVjh2Y+9kc43OQdi5E/tUZtI5E6St9JO9kXq+tTt37YzJCrkCY5ZW9o+Dqe0HTi4eGCL+b11ZomYgrMQHA1HNDyS2ngQJtbT1ZuVdzBh81XZbhyVIljjDUXkam9bb09yx8ukWKoV6DaH27OeSi9mHv0iqEhi5pJyfB9yCP0990mEXR2ctfcisHQvYAJ41D9X4QM7mkAO0CTmKh6UA9FgrfV8fZmF9rFh9CMDzpFauSCqpVnjV3QTQcprbJ5rO0u6nI9fIf54BujGah1Euz1JbQtzTmzLuLajGSQBqbYG4hjU5TwoavfYAtJHcuW0mvf+LgZDTGrRMU6iOHXA3fBwHEDc8CHy+iQDRu2kYUVEdWrWyz8OExackJLWx2JBSKH0QOluUfALLtmRaQB2QMq0ediNAkOdmIxmgY9gs/f6SyY0FTkyQqmS7R7O8lsc+EaSIAyYqgPqb6u72IoDnuf2fRi3c9+0MieTYrDa+OUymH5cFAzgwyCi9qWuRA3BkJve4j/C4i8XYzlyStCJyv671xlXkbL/dnWV2XID7J8R+ZjMvvmEndCpzD0Rtye1887oZZFWgTj0bMb5QrK0HYqGU/rzhbyXGbJ/fk/3xhNLs8Y6YfOh+oKuGsY2q56wnB6QwclOA4Fiqt1v25AulRrMOnNSfKkgA3LKmOb7p5IEovlYtoqW4r1QzeNzT2iEmsH2iX145gDsTMAHm9FeYS1CnyIoQsgqjMS4TiuaxXVz8Q0LsSenTzbJd32C9orxfL8ZL6ZswgI5ttoS4rzFMBgTtfWcXQ2ERr0PoWNUBNhlTTCnFz37mCYYOfoIqEmq5LcDayd28w8dReWRlak9vABmI+VL1TWEfKK3P7Xo5CMNjx04wOH8B/Ngxrk3k8DeBW0yFYNPHW/QYYmYUvNDHMsIdH0i5MQmPuhxKjANipXIJxYpe2sTJnZWCtsKyfGWkVOfflg6uQ2PUkjQvPmSpZOYn+xubwejEODK8GfIWtZHnNdQCF843nbaHZsJaT8ePf0zuug+LcNrSUjItuaXOh1cvvQRNUaQVOm4o56se8Qihuj0m97yBb8HE2r+Nq3uvS25vO0jZ4r9Nrbcuoy0xBfWda6Agaei+AsoxoDsSPljE6tVfWySW5V5MqxHbhaNaiX77VvgjF6w3P7+IbPYr7bxXqI4kK+axbxRXvPJMzuQQBGktKGWDiNpERvqLD5EerEjl17ofTdRDLJ4MMNV5z1Wu/CC23PmeOmTMIcbpSN461Q0V438h3gLlpYFa7DIdR0U0siaTyezL+d6D2FSOgr/kmtF4PFWhDPx1dhfTyX0uAGjTpQogfgn7EE7qeEVrgGt85ff/+bwTs3e+VVneDzgfJJqKyI07mjcxlD8ZR29zhuuVVjNWRU2lwM89IHQhcVyTK3xcV0qKpuSwdS9Tsw1NHGe4WjAT/0em6mDsABarWJW0CDEKuFBFYiA/2AvW5NRQ4/rdkVd/dtiiUOKsTQ8dcHfzvN5aeaF5vNURVDESRifBLHxoDD0FgbE2cMHy2Nf4spRrTAcuV3s3wNBuUcPFGFOXjM88BqhoJE9i/8KMU8/qgfBjCbKinKqi/TnUJOH6dY6EcKf8ZaMOOs/e39lDQ40zafU3dI+H8Jw67H9z4GaJ+3483HCVXXWPr/MXeHqEjXSefEMB1nULhlK8bWMiiK7Sry0wtRNMpzJQj91Re9nzRm8A1RVOVO3Rwf2oUXv0p50VriDLD5oR2zGZkml1oCLJ18KT3FDQSv+y8aWkG7N6vCTI6wYQUV4p9toiDha2C1Z5auL7+Dm4CNYm70XJYi4f4OwYt4LP9f9FxTv8CF2Ke8KjCUkoA5TYbJBz0oGEJ8dAigVmqHJnEmiLHttry58/aUVFCMmZFVSOkKTH7h+SlDXKhgW5LZyQkMMCequLgcU0aNWYLytSiDmm/tCcIcFxijV1UpC475bTsaVZDZ5aiF4GUW2S5Vhlw/NCoY0q81oxaHuiQUPKmOyALcyAMa3aRCn4MrMBRrimwjOXU8M9vFvWjBplm9IrIcAprTNxPJyDivv7VfbKbrk4Al8KAXg31zJ6KuuRivuu7Qfbetloaa28tT/jfewIqPf434GxljTOjDCN/u1YRFUT73h5M89eUfahLB/ZkjPZN3x21aP1oAxl9AknVHQt0ilS+YUuy44LkTEUS2Q7pz/ckTf5D+QYGaLBOy+0mL9BOiwvkxJ+2oLTGj32FF+kjPP3uMTd1ZY5BXZ6PWqFh3Wwlyyj8PttdDqirPU+1EdYTV7UH9BPH1umarBpsZ6xq/YgsV+sO3iiy/CIxyf7xJ4D9BsfCLGddaaPvDaJ6UwUn8/+Khyn/IYypAhWa6h54zfNTY5Yaaf4JZxFvhueSw3jB2BMA+Ke8YcGzcT95hb6buhrPuzH5p3J7n9xXtsd3a+HYVgecipiPNPVe8pQEEOKyaXFKUeyDh+1rrhTSbtfM6DsRZ4mxYsbvQJKe3Mr39QXucYaEbFonhUCwAiZRHSwk638lv+zHaw9VkchdK6bDwETDq++W99+GIBscp3ikRUu/+7zMlZjr+3HBTO05SPu0tOi9Qxwa/PM+6oIGC2hRbqWdyOQ4RVO35SGfIeqmjdOo6V780IWFj0MtqX1I4REt68lTbKTy2TLAisMltu6MQosfaw5hnlRD9NjPtDfStWDawVRqWKCX5xqb6tgFn74NzbIxHVkiLmpyDyaBux5WgI8IVKHI5UBZJW+cK9qw3xzvXwFPM5tvAVKTewNCc6RJAEw3P5vzG6D9cYpFKc7+kaBosv/XzLsZnL6zTflJ2UKKfFL1mOG4+Mv1os7HjRTWcK5c1y7Kr25vYvINBeZMvojvr4iqrzgvz0bEclAl9LKaojORmYgCldDALkMBbmWtE1ubRTV2mjELmOS5e1126qF5fDmv7iRgH3sPvN/2O7WY7f7N/nOaFOW/TF0NSqwLeHVMC03TlawmgLCWDGCOzK0AKHQdZwBD6Sq0ak36UEYp7C0O5U5UJUJr02rV9w+U/0eJc/CMl49RvZxx5F1zqsSfVaO/uFMFMEFDLBNI9oBePdHtWMAXBUrMcP6DIk8IO07mc9xslkwApAKsv2SoBQXhFzNFgASGDcy9j4qPpDxOCvnMfj1YAsd4rmJgxX/4as61F/VZAqGhzwQSqFSslpFwPMTQRSfnthxKPYMvPtpW4A+JywrSx17TVLEebNMaiI9fVDV3SMRyd2RIr084MydhDJDHdbqL7tzY8zrosOAU9gFj9tmFhd0xl51QonPsRdS9ugaa26QKinrAUR3xP+b0aHcZnFtJiaOSZPzDYhjbz/Pt564b/ZU3qlOfa8jAju+GJ2TXEWY1hndivUU7GnDQXh1iIeLUC1IGKA6Cn+MeN+AWz4zh1jwv+gWhOkN0gIYeXYf7wWG93VmQbh9Drfr5QBjsVJpAgfv4gtQADIpSqQfqp7LsSVgU0+a5dBGCc59EFJhHguHxY6kxGkiiUmKtxIpyMktIziYUsKFJyHKXsAW3gqP1cVgilf6kpjK4Fit9CoQIS6h6iZT5w1cM1OSkK+qIw3PUo2c/sNaAo2pQYmFk58Svch52sO/3P4edQYu/qnGDwzhEtI/uipdR8Id3flXbNMXX7Qz0z3MLdbk4hkOWn6+3GgkVP2rL4yDgXWA8aa4fg1elVuEPlXRTvjq+cJPpQHrOUNN7pvXWByoD5HT91mYS7BVbjqSVKFOdbB1bTOVm6MwU1GEIuQBHFyGL8mNAkSf/p90fmQhsJhlJTLx3fbsK6k5ty2jHtbS+Rp9v7xyUf/Po7YyUERwpNyj9UpQDc4MBYv/wa/WYWVhYYSOVC57JVB7TfWK5BE/i7ZmcABH/q+e3xT+jKXHufZxUjjuavbLrRBe5E6k4o2ry29MWHk5MbI3FE8agfSFQtMH44y714EL/k7OMqOOE9bCTJkjNSSR0xg2SE2nLNghjfU81Tilc2WFkxuEHOlN2a5FLSvUjJ/UHDxOXiNYZrqYDSS8R216S7XwRhOkFq29EGU4KGoPD51NmJtK0wgYiA6oN04NlxhSOPsudE6dphH0FhUVpiEwRFoG/AAruMKW8cNCPTSUPlxaNapAQmCsBJrCWNM82H0BTt+8e3m24tuYhZXNAf7MPE/lzGlEK44Y8ywq36fJNi3K3jAsAtIlYN8ScsBvNDUtxq7gQtSrRlcjBVVyByFqCsl/k8Cl9Jvgjl+0tO+90Db26nko9bID0MDsPg0+rUUZx/SJqYBaCG2kMa4xkIuoPhCJKkGsGPgdIoXo1bqVuH/Zm+wsIM8aGndLkZrvYa8Snys4v0PyX7kv0x6Oy6NyH7cW0uM67qNwNi1fh9RS2QLCy4Mb/lsHaqmxc5ED9UPQ0hDMMFSLL06lLlVYKINj9EUeWYDgkNjTPiC4jaTm97wjdSH6UNUK9ZpmFyWHXYgdvQkPWPDL9QOVs9EMJNP4BGC9HwhWVob3Z21WVX7vx8lKI+K1E/wgRdvT4tqDE+EwQ5AAUNnb9RlnJxEeWD0VbXv2QT2nx3073iaIw+5JLfeqBxY/c+JDOogPvWWGBQzNfRTR2H66zof/bfbW2KfVLLzI5t1ETCjdmqL5aE3dCVPCCeMRLZQLdWPq9jhwP5kBbvyi3Pc2/ulOdGQiT8scOketR6tLuFq1GBMjjh1Yj7rphcpqkHJujrC1CY2WlPllPs9MepAL1Spk60u4frDpxBJ9ltdtnM7T/hL7cmj6bHOPEFf0PCltPFpCK+ILrXUPyjnAxr7XINMDxbPZv+lYk5Wgf6USsxzX3CvMC9fQR4x6gxyXwHrcLGujX0a3gGHPqoheWMx0iwZPGzd1Zehd+fS5yw4s7u6ls4UFQfRLURQ2UMZ4KdOlZ45S6b+koMhqDr5Wk9Lt46iB2oopVnyfetRCO14vjOBNYznuLpJXiFAo8GtgPRHNxt8idwZ6HWTEjqwmAmPoyK1AnnQvg2Amghe3sEISvBIyDrLGX3q5LLWmHTRgBkxhR2DLE/OugqXNbMlGmj3urJ6+E2xDFVT5cSgNTbN953zfwxZd5gS+dbLeIIr8utSLD1VJZBjWacA9Gebco1Fmq3UKha3XDxkLQl6wqvDQjWLlvUpPgbKLGaynuf65CuxGoFjWp1hN7+7noTiige2BCz3QovRkORkWDBMA+CO95MC7glT9xsakG+T38+wuFT+PDOXglG3HGzP/wDGD9CAlYrRFSrj3h0qV3OpF9TI+NIqlpDNc4HhrNy9fS3zP84SNmru51hGl+eIzR2/a/g6pQ40CATz9y+o+b+1AX2N1lcR+OlqLrXzEboicaq1S3wsVQKZFYXZbh284C0LlhvOY8PaqguvL84qvHA3XCOVeOgpLMPHQ5cLkinaS6mwwQJPNSPXRvcmrxGjGfxDJARAtBZDLLLsS3zrcaUY9q02YIAVf90F13y0zrgr8dr0L1kB2tbzXRZFPwaRY3SUaP7TB5G1vkmQcWQxLO2dA6d1DXBJzW6Z0nb+VC37KhCI9xzkPb9yKfdeh43QqVLT351M4G9v7bKTJF/4adGEvV8/aQ4TAUu7I04chm5glNs1EiU0SY+S3+rVxN32jnsvbTO+OGEXfhmrWgWHw2mhXO8aII2OtvhzmSvbkVte4XMhHksHOG7oPEdUlYeYlKDKZwXt7hwAVxBHWQkVNI3Q5wHeql7RbgoYoMtbJ9ycvJhPtQzyHoSb2Fv1tiCOJBV+h/o+6ZjqNohvKDQPE4AQj2xYcbXy/DxrGflNBoqOTj9OSTu/66920S/dmS2FHL8BELmeFbWALtIU9w3fgHqFw+r+ioSmcCZa2Dmok0zpuutofMo2Z1Vog1ZhbZljvSa13+ncRafgaSOcl562EPk0zqDJPBEfm2++uBBV9plnf8nY1dQymqdPwlIXgbgxrDn1Q74vThpO/qvWheLqkLkWmELV+Q0IrS3NM6RlVm6etZw8OQi9foRujWXmOLo29SNUhq+nf1pCasiY1NzfQSCvihVdqvcao2uOCskyJlzeoV1vsZnbAZ3XUbqaKqRE/Oo4tMoWHVESGRYAlEX9T/S3HRRURjHjNhYwBK4J2BtibisoY2baKFMBXr37kbaHkhT2D+OsiAFf7AYsbzADQZmR+YSTP497G4dU+CFucDgO6a6kSwiXiTKCvAoDnNXiKRdS6+3xtoXmSQMK7d2fXgC4CNOzQFX/li4q06XfxEdweRTf352ggBs4NEq8BIcZF/3l065o7lJ2F6IDGpuhBKYT1uYY1lhAywGp9mjkV4+nNbWAxbkPbR+RA0hfb1THF/wnF3DzUnHT0CoBQSFe/dMzuH8BPeJ79Grtqa7EAYzojAn3AwQ/7lR5zPT0NYYgIgWgGZ7cR4/GSnfQob9AIP0jtqxm+RNJgHuQVg7zp1WOf6M/G9ZBEdoY3teWManrF6vS6lizSz9WP0+48lspn7BYvFgEE2PDnZ9RKc0mNWCsWltTdKfcV0A0DUBmQV8lbM2xLpUjhCi9IhyZxOUo57ArGsN6pwimkFGd+qdWMllYtnJHjmSmcax9BNEQivOgEGL4RQEKJocJm7CaO14U2gLMlv6a6d+VrBc2inZZHs/PFAxEBKmJTcHP1vAemEdEVFQHC0fuOe0GL9fmkion79AL/QXGoadYDAy805wfJdxWsTAmcHziLiDvEIahGIfqwoo5g/QXiEThzGUbVbmV0rpLvwkIeNj+oJQVwHmLJAVui4IWDXz/HrUks9kpfYCwaud7Neqyn3wXao1gwi2rL3xecdB9+9CBzxJoujqE/yz7GNV6iYbVbEcPtK3766yzsQqU+kRF6stEnq4eGJAY5zTBcxip1FJjM++pLXIFWv4dSfViZ9RBkPw2MD7HuwAEns8+mY9tKEY9cXR79xcevcFdorMGPTbCf8dOZ58YHc8QmwSwdYUdtTTSkuyatxNdep7Zyds3gM4le+Bc8GbnonWI8/Xm34TuKxNnAfId6k21joF9t6lQ0Iombl3JFZh6J500bT35uj41fmXGXWN8WX24axQzNwlDxDmBiPE3fwp0u9rh3zjAmWxMGdZUBNG2otsSQ7wj2iYci+5mgGlu83OaUJCAx2BnDcG/I2QBkyz4OvHh/e1EXMLWFSnnSxg3QXnjwBZBldT0WUXRQ0+mznERq9BAHSwvAhqewNTa2qoMkVae58IYMJy6G/+p7lNqfu4A15XnFj8oxgm/YsTU42TCfo1tsI17bTaLYZaNkuu91Wje0xW6MbGT+5iUJOUL7xH5l/yo+F1FJHTcu7FgPldOBu7CgECiVt2jv3+vD+OpaYq2Voad75kNxxSIbeQMaJR5+RBS1oAX/M5jiPHpHlaTUux3//lwKUoiVEq5Unudipgg5J/GWZ0Z6IfVYV9JOmSMGlYIP5QXH49K6A9VfL/2g5SHNWhv+m5s7KGdo399AeuTdUyMEztLxCXvvaMXw1mbs/mDCCViSdhucTfLFxhrNaRHqulXT0F7ZBS8u7f7TK+Rd0VojvUpZMFp+XITs99Q1g6v/cU6Wi9sFJf+/MGW/9PKqahLTt71DzkDy4T1lJuMThik5ZqWY81BTWlvAOLuKSY7dHg6Wa1A6y+BMhUl3gMxB/mtu24uJL9hqXEMaO6Bqgz6YmMjGDbPyFib4J9NH9yPoeuH1+6I2glbFw9LOeytngIYVPxKes/Neh/HDxhIPYQ2fLO7QG/xr+R0Z9sukKtghgnMOT1GDl4Bu/EYV2qsBqQRR+KVj3cJg4azKt7muWgxp+ageJ0ol/U7E5lfyGhghCnz6q1JSjc0pK0S36IzGCsBxVlv/3EieIiIk+4+3zpnfJmGX1CNfiMcxX1q+Dxr8X/h66JSQhKQSPA2XFxvzGp3X73Pivt/DpUBy21IIH4uXGvLarcTAuMSMDRlHo5SUq3HCz1ZCVbTHYyifh+gTNE4py4MmNnJBigCPzcxtrVN5f+kNfBVINO0La7coQwp7VrKDl65ekszDvKxO1LkE/iUBTtjZLkioN27IZ3W2skwgNYQ/ad/qAHgQg2fBXCerYjISVtkQc86yomGJYeV+P91vBAccC/c3Ve+DrF4ZxLU+P6Wo/TFaX2gjR/O9ETJgMYFivDMz/eSTtbp/lOMM84fWOWn7/uco1egYFD76QEqBHmUdWsSSffduIgf/EEsQlM6y5g4wt4fq2BB0p+JCKYyFWocjRFjM1TqQaCuuFl7gefUjXUe5c4os5mjogD3QkMgSNLRdwyFNIbXcsM40">
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['Form1'];
if (!theForm) {
    theForm = document.Form1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/WebResource.axd?d=pynGkmcFUV13He1Qd6_TZBKS046wTMyigCWLXS9CoObdwNJWG1kAT1qDVepJiIsK0oJyAQ2&amp;t=637811765229275428" type="text/javascript"></script>

<script language="javascript">var facrConfig = {rootUrl: '/' , login: 0};</script>
<script src="/ScriptResource.axd?d=NJmAwtEo3Ipnlaxl6CMhvoUsZX3mHs7zJQFeNVNw9Wbd6qHcinMMZfv_N1FVKHxSs-FQrKtXsyFcW5PLRbkCSk7QS2YpG2cnGZa8lRx9IyC2X7K1cObloFMnrrrTZbBKEVCAI8dkd4Ejd-sNYulJDsEF1uU1&amp;t=ffffffffaa493ab8" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=dwY9oWetJoJoVpgL6Zq8OCuNMoZUKfSdk5hm6iCeBFrHX8Ep4ePVwFurZvgLmIVx1c5WPjiY3MyYQlu9SmQeK6j1d1HTpY46xnMam9WtQtcHipM7Vqi1mPtitrVPrufA0AX3Wg-qM9pBJXF9CbH8V5C-UBM1&amp;t=ffffffffaa493ab8" type="text/javascript"></script>
<script src="../js/FixFocus.js" type="text/javascript"></script>
<script src="../js/jquery-1.10.2.js" type="text/javascript"></script>
<script src="https://code.jquery.com/ui/1.10.4/jquery-ui.js" type="text/javascript"></script>
<script src="../js/jquery.custom.select.min.js" type="text/javascript"></script>
<script src="../js/jquery.numeric.js" type="text/javascript"></script>
<script src="../js/jquery.mousewheel-3.0.6.pack.js" type="text/javascript"></script>
<script src="../js/jquery.fancybox.pack.js" type="text/javascript"></script>
<script src="../js/main.js" type="text/javascript"></script>
<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="6D316518">
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="ASMMGvKMWVJ7HJo0uidAwlUAn2Rk8XwxkBhqNFgT3v13dSkOov1yzqIjo1BZHv/429sLs5WLdcpmceUkhLIOWqtlJ0uVOPvZaKRW39XSgB9SK84p">
</div>
        <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$ScriptManager1', 'Form1', [], [], [], 90, 'ctl00');
//]]>
</script>

        


        <!-- Obal -->
        <div class="outer">
            <div class="outer2">
                <div id="inner" class="inner with-bar" style="min-width: 1060px; min-height: 5588px; height: 5309px;">


                    <!-- Hlavicka -->
                    <div id="divHeader" class="header">
                        
      <div class="inset clearfix">          
        <a href="../" id="TopMenu_A1"><img src="../img/logo.png" id="TopMenu_Img1" alt="FAČR - Informační systém" class="logo" width="84" height="114"></a>
        <div id="TopMenu_dvNotLoged" class="title">
          <h3><a href="../" id="TopMenu_A2" style="color:White;text-decoration:none">Informační systém FAČR</a></h3> 
          <p><a href="../LogIn.aspx" style="font-size:14px;color:White;">Přihlášení</a></p>        
        </div>
       
<style>
    .header .title .admin-oddilu {display:inline;}
</style>

    

       <ul class="menu clearfix">
           <li class="uvod first"><a href="../">Úvod</a></li>
           
           <li class="podatelna"><a href="../clenove/podatelna.aspx" id="TopMenu_linkPodatelna">Podatelna</a></li>
            
           <li id="TopMenu_liLicencniSystem" class="licence"><a href="../kluby/licence-neprofi-kluby.aspx">Licenční <br>systém</a></li>

           <li id="TopMenu_liSoutez" class="soutez"><a href="prehled-soutezi.aspx">Soutěže</a></li>
           <li class="clenove"><a href="../clenove/databaze-clenu.aspx" id="TopMenu_A5">Databáze <br>členů</a></li>
           <li class="hraci"><a href="../hraci/prehled-hracu.aspx" id="TopMenu_liSeznamHracu">Přehled <br>hráčů</a></li>
           <li id="TopMenu_liPlatba" class="platba"><a href="../clenove/hromadny-doklad.aspx">Platba <br>členství</a></li>
           
           <li class="napoveda last"><a href="../clanky/vypis-clanku.aspx">Nápověda</a></li>           
       </ul>


      </div>


                    </div>
                    <!-- / Hlavicka -->

                    <hr>




                    <!-- Obsah -->
                    <div class="inner-content">
                        
                        
                        
    <script type="text/javascript">
        function closeDialog()
        {
            $.fancybox.close();
        }        
    </script>
    <style>
        .soutez-detail table.soutez-zapasy{border-collapse:collapse;}
        .soutez-detail table.soutez-zapasy td {border:solid 1px black;padding:5px 5px 5px 5px}
        .soutez-detail .nadpis span{float:right;}
        .kolo .nadpis {border-left:none;border-right:none;margin-right:0px;border-radius:0px 0px;font-size:15px;padding: 5px 5px 5px 10px}
        .list.zapasy {box-shadow:none;margin-bottom:8px;padding-left:4px;}
        .form fieldset table.soutez-zapasy {margin:0px;}
        td.spravce {font-weight:bold;}
        a.disabled{color:#a2a2a2}
        tr.type_true td{color:#aeaeae !important; text-decoration:line-through}
        .vlastni {color:black;font-weight:bold}
        .vlastni input {float:right;position:relative;top:1px}
        .penalta-ne{display:none;}
        .penalta-ano {display:inline;font-size:10px;}
        .soutez-zapasy th {text-align:center !important; border:solid 1px black !important}
    </style>

    
 <h1 class="nadpis-hlavni size-2">
        23  M-2/C
        <span class="help-info size-2">
            ročník 2022, A4C, Muži, číslo 2022110A4C<br>Neurčeno Hl. město Praha skupina C
        </span>
</h1>
    
    <div class="grid-row">
        <div class="col combine f-left" style="width: 800px; min-width: 800px;">

          
                    <div id="MainContent_panelBody">
	
                        <div class="form soutez-detail">
                              <h2>
                                Utkání soutěže
                                <i style="float: right">
                                    <span class="vlastni"><input id="MainContent_chcVlastni" type="checkbox" name="ctl00$MainContent$chcVlastni" onclick="javascript:setTimeout('__doPostBack(\'ctl00$MainContent$chcVlastni\',\'\')', 0)"><label for="MainContent_chcVlastni">pouze vlastní</label></span>
                                </i></h2>
                            <fieldset style="padding-bottom: 20px">
                                <legend>Detail soutěže</legend>
                          

                          

                            <table class="soutez-kola" style="margin:0px">
                                                        
                                
                                    <tbody><tr class="first odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">1. kolo
                                                    <span> 21.08.2022 17:00</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           20.08.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdDomaci_0" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdHoste_0" class="" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 5   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KYJE  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          UMT/T                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=cb0b2f5b-07ac-4d51-8064-64336b349e40&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=cb0b2f5b-07ac-4d51-8064-64336b349e40&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           20.08.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdDomaci_1" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdHoste_1" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          4 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          D.MĚCHOLUPY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=2427a903-53a5-4b1b-b245-e53521038f7d&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=2427a903-53a5-4b1b-b245-e53521038f7d&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           20.08.2022 11:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdDomaci_2" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdHoste_2" class="" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 6   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          CHOLUPICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=a31f61d1-53c0-4daf-9121-765a1e6ad2ee&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=a31f61d1-53c0-4daf-9121-765a1e6ad2ee&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           20.08.2022 13:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdDomaci_3" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdHoste_3" class="" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          <span style="color:red;font-size:10px;">Nedohráno za stavu:</span><br>1 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          VRŠOVICE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=eb8cf8a4-8a8b-4f89-a6d2-1dd1bd6f72d8&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=eb8cf8a4-8a8b-4f89-a6d2-1dd1bd6f72d8&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           20.08.2022 14:45
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdDomaci_4" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdHoste_4" class="" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 4   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          UHŘÍNĚVES  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=938ab385-2770-46b9-a60f-9fd578a0366b&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=938ab385-2770-46b9-a60f-9fd578a0366b&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           21.08.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdDomaci_5" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdHoste_5" class="" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          NUSLE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=b615fe88-a158-46a4-ad70-10fde28662e4&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=b615fe88-a158-46a4-ad70-10fde28662e4&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last">
                                                       <td style="width:100px" class="first">
                                                           01.09.2022 18:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdDomaci_6" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_0_tdHoste_6" class="" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          3 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          VRŠOVICE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkZapis_6" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=c2989d20-6058-4a20-bf40-501792758df7&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_0_linkdelegace_6" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=c2989d20-6058-4a20-bf40-501792758df7&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">2. kolo
                                                    <span> 28.08.2022 17:00</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           27.08.2022 10:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdDomaci_0" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdHoste_0" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          NUSLE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          SK Nusle                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=e495e0c8-db1f-4e0e-91c5-64ae63088064&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=e495e0c8-db1f-4e0e-91c5-64ae63088064&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           27.08.2022 11:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdDomaci_1" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdHoste_1" class="" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 6   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          CHOLUPICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7d74ce20-a5c1-4eb5-a83c-83fb3e23c726&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7d74ce20-a5c1-4eb5-a83c-83fb3e23c726&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           27.08.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdDomaci_2" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdHoste_2" class="" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          STODŮLKY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=9cf67091-3de7-43bb-baa0-2601199ac43f&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=9cf67091-3de7-43bb-baa0-2601199ac43f&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           27.08.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdDomaci_3" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdHoste_3" class="" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          <span style="color:red;">Nezahájeno</span><br>   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MALEŠICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=bf7755ef-9fa0-4e50-8377-6c7cfa2c8004&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=bf7755ef-9fa0-4e50-8377-6c7cfa2c8004&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           28.08.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdDomaci_4" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdHoste_4" class="" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          3 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          DUBEČ  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=9f5b9d73-cd29-4890-840b-89b6469cb13d&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=9f5b9d73-cd29-4890-840b-89b6469cb13d&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           29.08.2022 18:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdDomaci_5" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdHoste_5" class="" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 3   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KOLODĚJE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                           / , Původní termín: 28.08.2022 17:00                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7feef384-c9d7-4b82-b591-87e5ea97dbe6&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7feef384-c9d7-4b82-b591-87e5ea97dbe6&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last">
                                                       <td style="width:100px" class="first">
                                                           08.09.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdDomaci_6" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_1_tdHoste_6" class="" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          6 : 4   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MALEŠICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkZapis_6" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=f684e925-f47b-4891-8668-7ecb9638ba9b&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_1_linkdelegace_6" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=f684e925-f47b-4891-8668-7ecb9638ba9b&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">3. kolo
                                                    <span> 04.09.2022 17:00</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           03.09.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdDomaci_0" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdHoste_0" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 3   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KYJE  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          UMT/T                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=f9cfe16d-74e3-4672-8ce2-e3461c49d21d&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=f9cfe16d-74e3-4672-8ce2-e3461c49d21d&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           03.09.2022 13:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdDomaci_1" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdHoste_1" class="" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          VRŠOVICE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=5a95a2e9-6cef-4da0-91a1-f9189cb596be&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=5a95a2e9-6cef-4da0-91a1-f9189cb596be&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           03.09.2022 15:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdDomaci_2" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdHoste_2" class="" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 6   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          UHŘÍNĚVES  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=0de1d726-99f9-40a4-b8ec-5407809901af&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=0de1d726-99f9-40a4-b8ec-5407809901af&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           04.09.2022 14:45
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdDomaci_3" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdHoste_3" class="" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 6   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          TJ PRAGA / tráva                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=a2635236-03a6-48ea-8a6c-399629dda0c3&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=a2635236-03a6-48ea-8a6c-399629dda0c3&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           04.09.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdDomaci_4" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdHoste_4" class="" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          7 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          NUSLE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7368f2b8-7f5e-4c87-8034-79344157e217&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7368f2b8-7f5e-4c87-8034-79344157e217&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           04.09.2022 17:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdDomaci_5" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_2_tdHoste_5" class="" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          3 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          D.MĚCHOLUPY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          , Původní termín: 04.09.2022 16:15                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7987533b-0347-45ce-b550-c31672723dc2&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_2_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7987533b-0347-45ce-b550-c31672723dc2&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">4. kolo
                                                    <span> 11.09.2022 17:00</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           10.09.2022 10:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdDomaci_0" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdHoste_0" class="" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          5 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          STODŮLKY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          , Původní termín: 10.09.2022 17:00                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=1b5b5ec9-d9b0-4211-89c7-edcf35a4c28c&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=1b5b5ec9-d9b0-4211-89c7-edcf35a4c28c&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           10.09.2022 11:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdDomaci_1" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdHoste_1" class="" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          3 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          CHOLUPICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=610f1527-25b9-4eaa-b8af-65a71e48e452&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=610f1527-25b9-4eaa-b8af-65a71e48e452&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           10.09.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdDomaci_2" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdHoste_2" class="" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 4   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          DUBEČ  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=489e45e9-bdf2-4c72-b8de-a054b8ec0c91&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=489e45e9-bdf2-4c72-b8de-a054b8ec0c91&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           10.09.2022 17:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdDomaci_3" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdHoste_3" class="" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MALEŠICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=947b06b9-fe96-4e5d-824b-4ff992c901f7&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=947b06b9-fe96-4e5d-824b-4ff992c901f7&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           11.09.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdDomaci_4" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdHoste_4" class="" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 3   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          D.MĚCHOLUPY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=a94de62a-5b63-4cce-bd0b-0de33e52c0d8&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=a94de62a-5b63-4cce-bd0b-0de33e52c0d8&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           11.09.2022 14:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdDomaci_5" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_3_tdHoste_5" class="" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 4   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MIKULOVA  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                           /  Hřiště: UMT Mikulova , Původní termín: 11.09.2022 17:00                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7ba9b91e-c0d3-494a-a1cd-97132b715547&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_3_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7ba9b91e-c0d3-494a-a1cd-97132b715547&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">5. kolo
                                                    <span> 18.09.2022 16:30</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           17.09.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdDomaci_0" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdHoste_0" class="" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 5   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KYJE  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          UMT/T                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=af632f9d-a91a-4dfb-a9a7-8e335c09944b&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=af632f9d-a91a-4dfb-a9a7-8e335c09944b&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           17.09.2022 13:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdDomaci_1" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdHoste_1" class="" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          3 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          VRŠOVICE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=9ae4c7da-33e4-4e40-b0f0-0333fd8b5048&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=9ae4c7da-33e4-4e40-b0f0-0333fd8b5048&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           17.09.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdDomaci_2" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdHoste_2" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 5   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          UHŘÍNĚVES  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=89320b09-0c38-462e-9e57-9a6da33df4b3&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=89320b09-0c38-462e-9e57-9a6da33df4b3&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           18.09.2022 14:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdDomaci_3" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdHoste_3" class="" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          TJ PRAGA / tráva                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=bfd2f026-f0f2-4aba-a908-748060061e1b&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=bfd2f026-f0f2-4aba-a908-748060061e1b&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           18.09.2022 16:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdDomaci_4" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdHoste_4" class="" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          12 : 5   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KOLODĚJE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7bea2521-5900-46a3-80a7-2dbbb549a86f&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7bea2521-5900-46a3-80a7-2dbbb549a86f&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           18.09.2022 16:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdDomaci_5" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_4_tdHoste_5" class="" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          NUSLE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=b8c777fb-f439-4dd7-9a66-52ac05f77b2b&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_4_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=b8c777fb-f439-4dd7-9a66-52ac05f77b2b&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">6. kolo
                                                    <span> 25.09.2022 16:30</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           24.09.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdDomaci_0" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdHoste_0" class="" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          D.MĚCHOLUPY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=05bbeaec-8129-452a-8de2-d04ecdb145b6&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=05bbeaec-8129-452a-8de2-d04ecdb145b6&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           24.09.2022 11:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdDomaci_1" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdHoste_1" class="" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 4   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          CHOLUPICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=3e871e50-5014-4664-8ff2-c919df38db17&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=3e871e50-5014-4664-8ff2-c919df38db17&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           24.09.2022 16:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdDomaci_2" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdHoste_2" class="" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          STODŮLKY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=74e27610-c968-412b-902e-e87186424ce8&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=74e27610-c968-412b-902e-e87186424ce8&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           24.09.2022 16:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdDomaci_3" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdHoste_3" class="" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          3 : 9   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          DUBEČ  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=2833e3c9-5114-4246-9d7b-987c1dab5b11&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=2833e3c9-5114-4246-9d7b-987c1dab5b11&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           25.09.2022 14:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdDomaci_4" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdHoste_4" class="" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 5   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          SCHULHOFFOVA  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                           Hřiště: FK Dukla JM z.s. , Původní termín: 25.09.2022 14:30                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=695abef1-924d-4f28-ba07-468838b0c1c1&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=695abef1-924d-4f28-ba07-468838b0c1c1&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           25.09.2022 16:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdDomaci_5" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_5_tdHoste_5" class="" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          6 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          NUSLE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=ba212a1a-5983-4df9-a971-29f10004f8ab&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_5_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=ba212a1a-5983-4df9-a971-29f10004f8ab&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">7. kolo
                                                    <span> 02.10.2022 16:00</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           01.10.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdDomaci_0" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdHoste_0" class="" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KYJE  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          UMT/T                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=3b614efa-3b79-4d3d-b1f4-1170e38e4857&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=3b614efa-3b79-4d3d-b1f4-1170e38e4857&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           01.10.2022 13:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdDomaci_1" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdHoste_1" class="" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          8 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          VRŠOVICE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=f968e4f5-3bea-4f13-a2ae-dedb4c3a57f2&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=f968e4f5-3bea-4f13-a2ae-dedb4c3a57f2&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           01.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdDomaci_2" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdHoste_2" class="" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 6   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          UHŘÍNĚVES  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=9022750e-c71e-496e-80e0-e3be24575f02&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=9022750e-c71e-496e-80e0-e3be24575f02&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           01.10.2022 16:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdDomaci_3" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdHoste_3" class="" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          5 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MALEŠICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=53836d43-1367-463b-8079-833bc7b358f7&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=53836d43-1367-463b-8079-833bc7b358f7&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           02.10.2022 13:45
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdDomaci_4" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdHoste_4" class="" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          15 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          TJ PRAGA / tráva                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=8f83760f-c130-491f-a6bf-8942e0bb27a8&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=8f83760f-c130-491f-a6bf-8942e0bb27a8&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           02.10.2022 16:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdDomaci_5" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_6_tdHoste_5" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          5 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KOLODĚJE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=ea122b22-8be1-4cff-8517-bfa39ce6d28b&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_6_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=ea122b22-8be1-4cff-8517-bfa39ce6d28b&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">8. kolo
                                                    <span> 09.10.2022 16:00</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           08.10.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdDomaci_0" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdHoste_0" class="" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KYJE  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          UMT/T                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=5ca6a76a-5561-4aeb-807a-9b57c700a209&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=5ca6a76a-5561-4aeb-807a-9b57c700a209&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           08.10.2022 10:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdDomaci_1" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdHoste_1" class="" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 7   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          D.MĚCHOLUPY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=db85944d-c203-4ff3-88e0-0b983d6c098c&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=db85944d-c203-4ff3-88e0-0b983d6c098c&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           08.10.2022 11:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdDomaci_2" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdHoste_2" class="" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 3 (K)   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          CHOLUPICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7f27f72e-67a4-4e5a-b9f9-e303dc13b504&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7f27f72e-67a4-4e5a-b9f9-e303dc13b504&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           08.10.2022 14:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdDomaci_3" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdHoste_3" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          11 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MALEŠICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                           Hřiště: AFK Slavia Malešice, Původní termín: 09.10.2022 14:30                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7877aade-1cc7-446f-8d86-839e9b888534&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7877aade-1cc7-446f-8d86-839e9b888534&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           09.10.2022 16:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdDomaci_4" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdHoste_4" class="" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          DUBEČ  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=1d7793f1-29b8-4e0c-b810-5dd533746af6&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=1d7793f1-29b8-4e0c-b810-5dd533746af6&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           09.10.2022 16:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdDomaci_5" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_7_tdHoste_5" class="" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          NUSLE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=b89a9a3f-c8f1-4a5a-96b8-c3f7f372188e&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_7_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=b89a9a3f-c8f1-4a5a-96b8-c3f7f372188e&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">9. kolo
                                                    <span> 16.10.2022 15:30</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           15.10.2022 13:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdDomaci_0" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdHoste_0" class="" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          3 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          VRŠOVICE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=307bd92a-087d-4340-a6cb-e2db5af53f2c&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=307bd92a-087d-4340-a6cb-e2db5af53f2c&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           15.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdDomaci_1" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdHoste_1" class="" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          9 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          UHŘÍNĚVES  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=0158242a-5173-4803-b81f-ac9fc2257a53&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=0158242a-5173-4803-b81f-ac9fc2257a53&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           15.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdDomaci_2" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdHoste_2" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          7 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          STODŮLKY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7efac94d-58c5-491a-b5ae-3f0abf205a69&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7efac94d-58c5-491a-b5ae-3f0abf205a69&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           15.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdDomaci_3" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdHoste_3" class="" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          11 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MALEŠICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=021d8c1c-7205-416b-a58a-21d437ee500c&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=021d8c1c-7205-416b-a58a-21d437ee500c&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           16.10.2022 13:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdDomaci_4" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdHoste_4" class="" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          5 : 3   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          TJ PRAGA / tráva                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=15e2c976-f1ee-44d4-b7f8-bb7a99f2ebd7&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=15e2c976-f1ee-44d4-b7f8-bb7a99f2ebd7&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           16.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdDomaci_5" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_8_tdHoste_5" class="" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KOLODĚJE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=5633264c-3fbf-47ac-ad72-8ad6922f9242&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_8_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=5633264c-3fbf-47ac-ad72-8ad6922f9242&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">10. kolo
                                                    <span> 23.10.2022 15:30</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           22.10.2022 11:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdDomaci_0" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdHoste_0" class="" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          0 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          CHOLUPICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=ef66fbe5-01ca-405a-9422-4ff029009423&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=ef66fbe5-01ca-405a-9422-4ff029009423&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           22.10.2022 13:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdDomaci_1" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdHoste_1" class="" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          7 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          VRŠOVICE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=21eb50e5-eb4b-421a-a780-e70aae18dca7&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=21eb50e5-eb4b-421a-a780-e70aae18dca7&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           22.10.2022 15:00
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdDomaci_2" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdHoste_2" class="" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 3   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          D.MĚCHOLUPY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=849b2bee-8347-4283-a8e5-a815c451125d&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=849b2bee-8347-4283-a8e5-a815c451125d&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           23.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdDomaci_3" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdHoste_3" class="" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KYJE  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                          UMT/T                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=c7efca65-df3f-40f2-9539-df6a80ef03bb&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=c7efca65-df3f-40f2-9539-df6a80ef03bb&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           23.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdDomaci_4" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdHoste_4" class="" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          5 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          DUBEČ  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=caceae7f-b5ba-4252-9a5d-4af1e56da52a&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=caceae7f-b5ba-4252-9a5d-4af1e56da52a&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           23.10.2022 15:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdDomaci_5" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_9_tdHoste_5" class="" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          NUSLE   T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=6ce79ede-e8f6-4518-9162-19181e09a2a4&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_9_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=6ce79ede-e8f6-4518-9162-19181e09a2a4&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                                    <tr class="odd">
                                        <td colspan="2" class="kolo first last" style="padding-right:0px">
                                            <div class="head clearfix">
                                                <h2 class="nadpis">11. kolo
                                                    <span> 30.10.2022 14:30</span>
                                                </h2>
                                                <div class="clear"></div>
                                                </div>
                                        </td>
                                    </tr>
                                    <tr class="last">
                                        <td colspan="2" class="first last">
                                            <div class="list zapasy">
                                            <table class="soutez-zapasy">
                                            
                                                    <tbody><tr class="first odd">
                                                        <th class="first">datum a čas</th>
                                                        <th>domácí</th>
                                                        <th>hosté</th>
                                                        <th>skóre</th>
                                                        <th>hřiště</th>
                                                        <th>pzn.</th>
                                                        <th class="last">akce</th>
                                                    </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           28.09.2022 10:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdDomaci_0" style="width:150px">
                                                           TJ Sokol Stodůlky z.s.  "B" <i>(10)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdHoste_0" class="" style="width:150px">
                                                           Sportovní klub Dolní Měcholupy,o.s. <i>(2)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          1 : 1   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          STODŮLKY  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkZapis_0" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=5bfca71e-ba45-4732-b969-24a8869b1695&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkdelegace_0" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=5bfca71e-ba45-4732-b969-24a8869b1695&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           29.10.2022 14:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdDomaci_1" style="width:150px">
                                                           FK Slavoj Koloděje, z.s. <i>(8)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdHoste_1" class="" style="width:150px">
                                                           Tělovýchovná jednota Kyje Praha 14   "B" <i>(4)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          5 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          KOLODĚJE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                           / , Původní termín: 30.10.2022 14:30                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkZapis_1" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=7b7d0efb-214a-48af-9c8c-52e67361bc5a&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkdelegace_1" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=7b7d0efb-214a-48af-9c8c-52e67361bc5a&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           29.10.2022 14:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdDomaci_2" style="width:150px">
                                                           Tělovýchovná jednota SOKOL BENICE <i>(6)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdHoste_2" class="" style="width:150px">
                                                           Fotbalový klub Čechie Dubeč, z.s.  "B" <i>(12)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          6 : 3   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          UHŘÍNĚVES  UMT.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkZapis_2" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=505dd48d-5328-40b9-ab24-a9bf23f73ae2&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkdelegace_2" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=505dd48d-5328-40b9-ab24-a9bf23f73ae2&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false odd">
                                                       <td style="width:100px" class="first">
                                                           29.10.2022 14:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdDomaci_3" style="width:150px">
                                                           AFK SLAVIA MALEŠICE <i>(9)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdHoste_3" class="" style="width:150px">
                                                           SK NUSLE z.s. <i>(3)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          2 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          MALEŠICE  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkZapis_3" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=1ec0b5da-ae58-4be9-a738-a0ff3c671cec&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkdelegace_3" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=1ec0b5da-ae58-4be9-a738-a0ff3c671cec&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false">
                                                       <td style="width:100px" class="first">
                                                           30.10.2022 12:15
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdDomaci_4" style="width:150px">
                                                           Tělovýchovná jednota PRAGA  "C" <i>(7)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdHoste_4" class="" style="width:150px">
                                                           Sportovní klub Union Vršovice, z.s.  "B" <i>(5)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          4 : 2   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          TJ PRAGA / tráva                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                                                                                     
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkZapis_4" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=e0dcd676-2c78-4393-8c5e-defccc0bd1e6&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkdelegace_4" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=e0dcd676-2c78-4393-8c5e-defccc0bd1e6&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                                   <tr class="type_false last odd">
                                                       <td style="width:100px" class="first">
                                                           30.10.2022 14:30
                                                       </td>

                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdDomaci_5" style="width:150px">
                                                           FK Dukla Jižní Město z.s.  "B" <i>(11)</i>
                                                       </td>
	
                                                       
                                                       <td id="MainContent_rptKolaSouteze_rptZapasy_10_tdHoste_5" class="" style="width:150px">
                                                           TJ Sokol Cholupice, z.s.  "B" <i>(1)</i>
                                                       </td>
	
                                                       <td class="center" style="width:30px">
                                                          7 : 0   
                                                          <span class="penalta-ne"> (PK:0:0) <span>                                                 
                                                       </span></span></td>
                                                       <td class="center" style="width:80px">
                                                          SCHULHOFFOVA  T.                                                           
                                                       </td>
                                                        <td class="" style="width:90px">
                                                           /  Hřiště: FK Dukla JM - tráva, Původní termín: 30.10.2022 14:30                                                           
                                                       </td>
                                                       <td class="center last" style="width:auto">
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkZapis_5" class="detail_zadosti_popup uzavren" data-fancybox-type="iframe" href="../zapasy/zapis-o-utkani-report.aspx?zapas=f1f336e9-127f-43b9-99f3-7acb862e9465&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm">zápis uzavřen</a><br>
                                                           <a id="MainContent_rptKolaSouteze_rptZapasy_10_linkdelegace_5" class="detail_zadosti_popup" data-fancybox-type="iframe" href="../zapasy/zapas-delegace-report.aspx?zapas=f1f336e9-127f-43b9-99f3-7acb862e9465&amp;zapis=1&amp;hidemenu=1&amp;.htm">delegace</a><br>
                                                           

                                                       </td>
                                                   </tr>
                                                
                                            </tbody></table>                                            
                                                </div>
                                        </td>
                                    </tr>
                                
                            </tbody></table>
                              </fieldset>
                            
                        </div>

                    
</div>
              

        </div>
        <div class="col combine last" style="margin-left: 815px;">
         
<div class="popup box">
             <div class="inset clearfix">
                 
                 <div id="MainContent_soutezeRozcestnik_panelDetail">
	
                 <h3 id="MainContent_soutezeRozcestnik_nadpisSouteze">Podrobnosti soutěže č. 2022110A4C</h3>

                   <ul class="basic">
                      <li class="first">
                         <a id="MainContent_soutezeRozcestnik_listHitparady" href="hitparady-souteze.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6"><b>Hitparády</b></a>
                     </li>
                     <li>
                         <a id="MainContent_soutezeRozcestnik_linkZapasySouteze" href="detail-souteze.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6"><b>Utkání této soutěže podle kol</b></a>
                     </li>
                       <li>
                         <a id="MainContent_soutezeRozcestnik_linkZapasySoutezePodrobne" href="../zapasy/prehled-zapasu.aspx?soutez=ae9809e0-5712-4abd-b99a-997cf9d3d8c6"><b>Podrobný přehled utkání této soutěže</b></a>
                     </li>                     
                      <li id="MainContent_soutezeRozcestnik_liTybulkySouteze">
                         <a id="MainContent_soutezeRozcestnik_linkTybulkySouteze" href="tabulky-souteze.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6"><b>Tabulky této soutěže</b></a>
                     </li>
                       <li id="MainContent_soutezeRozcestnik_liStatHracu" class="last">
                         <a id="MainContent_soutezeRozcestnik_linkTybulkyStat" href="../hraci/statistiky.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6"><b>Statistiky hráčů</b></a>
                     </li>
                              
                 </ul>  
                     
</div>
                 <h3>Rychlá navigace soutěžemi</h3>
                 <ul class="basic">
                     <li class="first">
                        <a href="prehled-soutezi.aspx"><b>Soutěže</b> - vyhledání a přehled soutěží</a>
                     </li>
                      <li>
                        <a href="../zapasy/prehled-zapasu.aspx"><b>Utkání</b> - vyhledání a přehled utkání</a>
                     </li>
                     <li class="last"><strong>Výsledkový servis</strong> - vyhledejte požadovanou soutěž a otevřete její detail</li>
                 </ul>                 
             </div>
             <span class="corner pos-side-left top"></span>
         </div>

     <div>

             
</div>
        </div>
       
    </div>



                       

                    </div>


                    <!-- / Obsah -->

                    <hr>

                    <div id="divFooter" class="footer" style="">

                        
                        <div class="bg">
                            <ul>
                                <li class="first last">
                                    <a href="https://www.facebook.com/ClenstviFacr">FACEBOOK členství</a>
                                    <a href="https://clenstvi.fotbal.cz">clenstvi.fotbal.cz</a>
                                    <a href="https://www.fotbal.cz">fotbal.cz</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <!-- / Paticka -->
                </div>

            </div>

        </div>
        <!-- / Obaly -->

        <div id="dialog-msg" title="Info" style="display:none;">
            <p style="padding-top: 20px; text-align: center; font-size: 14px" id="dialog-msg-inner"></p>
        </div>

        <script type="text/javascript" language="javascript">
            Sys.WebForms.PageRequestManager.getInstance().add_endRequest(EndRequestHandler);
            function EndRequestHandler(sender, args) {
                if (args.get_error() != undefined) {
                    var errorMessage;
                    if (args.get_response().get_statusCode() == '200') {
                        errorMessage = args.get_error().message;
                    }
                    else {
                        errorMessage = 'Nespecifikovaná chyba. ';
                    }
                   
                    args.set_errorHandled(true);
                    alert('Omlouváme se, ale vyskytla se chyba. Je možné, že vám vypršela platnost přihlášení! Nyní budete přesměrování na https://is.fotbal.cz!\r\n');
                    //window.location = 'https://is.fotbal.cz';
                   
                }
            }
            if (facrConfig.login == 1) { setHeartbeat(); }
        </script>
    </form>


</body>
"""
prvni_zapis = """
<html xmlns="http://www.w3.org/1999/xhtml" class=""><head><title>
	IS FAČR
</title>
     <script type="text/javascript" async="" src="https://www.gstatic.com/recaptcha/releases/NJPGLzpIZgjszqyOymHUP0XR/recaptcha__cs.js" crossorigin="anonymous" integrity="sha384-ZYQoIqB/d7EcGEYcvlC9A7t1IpVWat2ohjT3M/Eet3ycTS19/UnN2DgNjWuE3vZH"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript">
        var messageInfo = { show: false, title: 'Upozornění', msg: '', type: '' };
        var messageEval = null;
        var boxLocalSelected = null;


        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date(); a = s.createElement(o),
        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

        ga('create', 'UA-38697170-2', 'fotbal.cz');
        ga('send', 'pageview');
        
    </script>

    
<link id="ContentPlaceHolderHead_Link2" rel="stylesheet" href="https://is.fotbal.cz//css/base.css" type="text/css">
<link id="ContentPlaceHolderHead_Link1" rel="stylesheet" href="https://is.fotbal.cz//css/zapis-utkani.css" type="text/css" media="screen, projection, tv">
    
<style type="text/css">.fancybox-margin{margin-right:0px;}</style></head>
<body class="has-js" style="">
    <form method="post" action="./zapis-o-utkani-report.aspx?zapas=cb0b2f5b-07ac-4d51-8064-64336b349e40&amp;zapis=1&amp;noprint=1&amp;btnprint=1&amp;.htm" id="form1">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="">
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="GLMDbSGSsP8W1vYtZPPQgPRCm2/6g+zWL8KrNQztD8QzXWyBm3wlEeiAuVDlePZgEyIMhrCEF4h0rmSjPjKF1+RFCjyiUElmi+jg8Ou76vksyBFAMhvckr3eEGqXRw3SEhbeDhPIM0oaKxEO5tQ38gzaEOgmpQ1DN+ztu9bL1pZuD6USpn69Px5WdseREmVkNeNkwBDBCpu0t7Lavv0vRBS/1Ck95JWPwfmtWDeTNd/nhB0NcnPPxCkREYaOt87Gv3Ytjbujr7RWs8ExIzijFvnhkErYXm7g7LpnUMyp4JDrchtqVz5Lr3j6WxyEuKDuFI1D1x1d9AVpumjVmO84cukOFlKAFdDLYS5NSLB2UjNCCI6zuYvFEfcKxubfmRNFAOFVcWj0hNxV8/6gSId/ItwvwThqQ8sNtG9qENIrE83b0vYpHqqHDpCfibXfBSut682pIZOluea1kIJxJTZCNoaLFeCFgNs8sLqLMb3Y+PH4OTRXZJPen6tAeslFWx2IiRMl/8H6xSp1WGUxKbHPybrb/5jPL7M89l6RtkgrbgTLGdkMMrqzKwwcedyfvdJtynl9j1wbXUukalJPWndUfmLnCCHEfa5k6K6KPdlDJsXE3Dwh5F/ddYWdxA93r88mTpCQO+qhpEfabCtb+fChgE7PZhr39juK6XCRJHRnCJfl7pwa/9Qf/6fFRzE7xRdjKdfOqMhSINIj4XLK44Z1UJ73OWJLTHX9UV6CM7dn4XmBOwC1B1n9wAjk4vlUKu4OfxzHFHiVRxvX/peCTsXceXU7tIrBXE1zS/HHWRS4naRlq3N1OUlMsZer4m1Z7eZ5ETb12aBJrmyo4RmwRFxKA6o3L3v65XHLELL5ilNZFL4Ew9yQq9hJltJuXf8zqRX7OYfAcVnPORPdYNLxLmUQujby3yKZVeqIHdJSTjdJu8n2rNNdbQayeyehvzbJo5thuSdzS2BdP2b9yF0oYgPKJp3PGwTqIoe/Ks4pICPfWc29cGgh7xa/1IYaF2O0Dz/ztzfPioYcL7m4HuqqM10T1vBxW8zlooztw2P/l9g8TB7/b7rF9SlmaLE1X7XZe0wwVjCiCAtJyKIflN6Jb/3Jie5FYM/ntOGHrHz5y+SHfrlUoOXVcpnS1au0Ql498af/paAEu4xROuo85P8QnE42HO/GZd8Gw78M+/Q/Pa/JdD+/dC9QAmud5keurdEyIl4d6VZJqCOnJYhv6aEGyioJ00OuJMd2F5/vSmrC42eK9xelJRcU/675ODcoxTrhStw9x3CFmr+UXBjnWRWNOFlVHU0110hbSLK0QVt0SZ1euL6IbJXcrO7o111hewCvhC/do0qeenhLEkV1Rcd2/u7qCS7muMpr62CYoL1oDF4FpU6dFwdbJARwUAORiC+HiMpt7YHoSG6+L2+Vjza8VYjnUtcaTjeBrGS4gGW3NWxAUfpi5IZZo2LZKFWC5ofCFkYKM0yq0jM7m1G57s6ml5kjamSTn+Zl7b3h6oKqhbHvxQyMOf1Kq3QJmZsKQRylP57UAyhgkWEFjxX7jBAziiRIhEQb6ATfyOO81M41Fm2tusmtcBc1kGxOSK5loyAut1AcersgI4Fk+zKkMYVDWU06pDHlvaVNxh6u+7ENEUQQfn7X2S5vms2OqN+An28Rfml8zlJdnhMWq8UFWpvaJOaW6FU2vkIdmz0UafMiwhKT7Zom/goXlS3fu0c6RtgCzeMbQopgSsk3gZPJtAnO/zqhszKf7T/b8elUc2Qt0SlhOTyQ6gk7v0QIpBV0pGtAT7kfyywzjWZU5bsky8rrmdX+YbDnia3nBAdG3mpXTEW1d+g8oC7QqRU5hdBrmJ5HxfNf4fHJ/cL2ZckN4xR8rVQJN+ZlCilhcm75Q4ttOCjwGhS5T1pBp4bEy1BHweQDdh793XpGch9F23YNQNVyt30+ZOJMjQU3HsgVsCRsJ2Ie4W4yltCdexG7kJfi90E8rA6/jHSCRfWwvjSk52gE5072J3l4JKC7FMYxRlZfGW6ZyqDM8pRI4Lp0Pq4NekDrgPE1ANfACResekrt91qYv6AAuyQ8ictlTf50RehpHHRXOTu87EHa0tpeqAFDDNPdxUAw+WyAdVdC73fmtTq35Kg4dfOTpbhEhSJOlrwtSAxvL3+hw0Gs5ceDjc5m1tcga4egqCITo/gCMjpu0xASn9yk2DNxzFmxZtdaRKWBmWKXkWJjwSkhgbfza86+NAPNNVVo8DrmBQJw9kuxl+FKm4ZweYMU/rs3mqIJkfH5OJLv5irlV2YeVL108sYuxRpyWqNjmrPQzX5NBapSCPt5jZ8G3+RkaB5wEM7u8fsbBZfqVumN3YADfEUKLxCqg4lYWAOBsQwIlDlLWcSDYJdV8phZ5yoW+CzlvnbaCNyH5lmzj9GhbNfpnMrKIfFCxK+qp+qnDZVet4AiPJP3wL2tMbT39z3OHXGUBdi8WIuwX6S3kI8hKfSeLqub2NQSN9HL5UN+mVW3/Gdy75EOPLpvMTPBr+HVZ9BIJdupvUsXz8kZ0vCeJixHmc0yHP7hjH6CQiN+vbJTt8M/DzXk6aF5gwQE3aa8hxkk7RzaDbDot9JskmxZOb8oWd1ukwpctF3tbNeHoQYvCqxz37rEyiqawU8Dahjl4EpFGRG+YtK87ir6BLkZvH6gMhYdtoe3F+rQly3dYDQOLR02FUzCiJ6n7LLYkHiH+Hmq/3M8b+9GBtdO77B4qAyZ/1Q+p6H4Wdqj8mHAmK/6lyrkUJSjivIslEWsOsOxHL1Rag444J0s92hR5VAuqFE2LwLny8cd81fUXwTPQ8+BjHxd4LK7wzRJfdMOANjMAKunSFkIAXi71ABCeRR6r+iOx/K7+ifci5x6+d3GpThcIKctKmI5u6+/dY6DbuDcoJmxGLMC/FFiR4TROGhmPKkYVUG5ej0cj0adi/VyWlnumO9xqBJ2sb43ztozLUzV8zIjZnSCJ/siIb2YDBpjOja8189h0bEXCFOR0wbYAdaI3ei6TKFf77xePsYQRG7eQZ6ycim4a9wpQWIEUThQtsN0N50YIFS6si3b9Amxixln/cGZDdNvOZhiNDV5lFcH82p4ygFgmd5v0RUiWCwAmbln9Yx0iRW5USs7+qg/zY+D1+CbjP56DEDl2Z0dTEKJjsOaXfT87vBdeiO0uMI4NdjHj/E7jB+LvrtnuQgpiLrubiLFxIL5Ox//dHsTkueXEX08JNligoKjKtR10hUWstu9YuDiaOFvfod7OfjeUVA3lingNpWx0e3G3dOlOvRnpt4Owpn1B+FiRUeqaW2Vsd93UdqycBtDenegD5G7m+5AJFr7Bu8/ISP2hwBFO/prONXaBKFICLVCjZ35gW6Of4Zf">
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['form1'];
if (!theForm) {
    theForm = document.form1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/WebResource.axd?d=pynGkmcFUV13He1Qd6_TZBKS046wTMyigCWLXS9CoObdwNJWG1kAT1qDVepJiIsK0oJyAQ2&amp;t=637811765229275428" type="text/javascript"></script>

<script language="javascript">var facrConfig = {rootUrl: '/' , login: 0};</script>
<script src="/ScriptResource.axd?d=NJmAwtEo3Ipnlaxl6CMhvoUsZX3mHs7zJQFeNVNw9Wbd6qHcinMMZfv_N1FVKHxSs-FQrKtXsyFcW5PLRbkCSk7QS2YpG2cnGZa8lRx9IyC2X7K1cObloFMnrrrTZbBKEVCAI8dkd4Ejd-sNYulJDsEF1uU1&amp;t=ffffffffaa493ab8" type="text/javascript"></script>
<script src="/ScriptResource.axd?d=dwY9oWetJoJoVpgL6Zq8OCuNMoZUKfSdk5hm6iCeBFrHX8Ep4ePVwFurZvgLmIVx1c5WPjiY3MyYQlu9SmQeK6j1d1HTpY46xnMam9WtQtcHipM7Vqi1mPtitrVPrufA0AX3Wg-qM9pBJXF9CbH8V5C-UBM1&amp;t=ffffffffaa493ab8" type="text/javascript"></script>
<script src="../js/FixFocus.js" type="text/javascript"></script>
<script src="../js/jquery-1.10.2.js" type="text/javascript"></script>
<script src="https://code.jquery.com/ui/1.10.4/jquery-ui.js" type="text/javascript"></script>
<script src="../js/jquery.custom.select.min.js" type="text/javascript"></script>
<script src="../js/jquery.numeric.js" type="text/javascript"></script>
<script src="../js/jquery.mousewheel-3.0.6.pack.js" type="text/javascript"></script>
<script src="../js/jquery.fancybox.pack.js" type="text/javascript"></script>
<script src="../js/main.js" type="text/javascript"></script>
<script src="https://www.google.com/recaptcha/api.js" type="text/javascript"></script>
      <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$ScriptManager1', 'form1', [], [], [], 90, 'ctl00');
//]]>
</script>

    <div>
       
        

    

    
<style>
    .zapis-report { background-color: white; width: 940px; padding:10px }
    table.vysledky { width: 937px;border:solid 2px black; margin-top:10px }
    .logo-report { width: 40px; }
    td,th { vertical-align: top; text-align: left; }
    .logo-text { font-size:14px;font-weight:bold;text-align:center; padding:3px 20px 0px 20px; font-style:italic; line-height:130% }
    .titulek { font-size:13pt;font-weight:bold;line-height:120%  }
    .titulek {border:solid 2px black;text-align:center; padding:7px 20px 5px 20px; height:44px; }
    .hlavicka-zaklad { border:solid 2px black; margin-left:10px; height:60px;}
    table.hlavicka-zaklad td,table.hlavicka-zaklad th{ padding:4px 2px 2px 2px }
    .vysledky td { padding:10px 4px 2px 4px; border:solid 1px black;font-size:14px; height:17px  }
    .hl1 { padding:4px 4px 2px 4px;; width:417px }
    .hl1 b{ font-size:19px; padding-left:20px }

    .w1 {width:30px }
    .clenid {text-align:center }
    .label { padding-right:15px;font-size:12px}
    .label.poradi2 {padding-left:20px }
    .vysledek-utkani { font-weight:bold;font-size:16px }
    .vysledek-utkani-polocas { font-size:16px }

    
    .vysledky.hraci th{ font-size:11px; border:solid 1px black;padding-top:5px;padding-left:5px}
    .vysledky.hraci td{padding:7px 4px 4px 4px; font-size:12px; border:solid 1px black;height:15px   }
    .vysledky.hraci tr.po11 td{border-bottom:solid 2px black }
    .asistence {padding-left:10px;font-style:italic; }
     .zapis-report h2 { padding: 2px 0px 2px 0px;margin:0px }
    .trest-popis { font-style:italic;}
    .vysledky p {line-height:120% }
    .hl1 p b{ font-size:13px; padding-left:0px }

    .vysledky.hraci .hodnoceni-rozhodcich td {border:none; }
    .vysledky.hraci .hodnoceni-rozhodcich td.val {padding-right:15px }
    .zapis-report { border-color: #184b7b #133f6b #092443; border-radius: 7px;
                     box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1), 0 1px 0 rgba(255, 255, 255, 0.3) inset }
    .kapitan {text-transform:uppercase;padding-top:5px; }
    tr.kapitanTrue td {font-weight:bold !important;  }
    .penalta{display:none;}
    .penalta.penalta-ano {display:inline;}
    .vysledky.hraci .odmeny td{font-size:12px!important;padding-top:2px;padding-bottom:1px;height:auto}

    @media print
{    
    .no-print, .no-print *
    {
        display: none !important;
    }
}
    .typ-6 td{color:red;font-weight:bold}
</style>
<div id="ContentPlaceHolderMaster_ZapisSouhrn1_panelPrint">
	
    <div class="no-print" style="text-align:center;padding:5px;">
        <input type="button" onclick="window.print();" value="Tisk">
        <input type="button" onclick=" window.location = 'zapis-o-utkani-report.aspx?zapas=' + document.getElementById('zapasReportDisplay').value + '&amp;zapis=1&amp;pdf=1';" value="Uložit jako PDF">
    </div>

</div>
<div class="book zapis-report">
    
        <input type="hidden" id="zapasReportDisplay" name="zapasReportDisplay" value=" cb0b2f5b-07ac-4d51-8064-64336b349e40">
    
    <table>
        <tbody><tr class="first last odd">
            <td class="first">
               
                <img src="https://is.fotbal.cz//media/FACR_logo_greyscale_1.JPG" id="ContentPlaceHolderMaster_ZapisSouhrn1_rptDetailZapasu_imgReport_0" class="logo-report">
            </td>
            <td class="logo-text">FOTBALOVÁ
                <br>
                ASOCIACE ČESKÉ
                <br>
                REPUBLIKY
            </td>
            <td>
                <div class="titulek">                   
                    ZÁPIS
                    <br>
                    O UTKÁNÍ
                </div>
            </td>
            <td class="last">
                <div>
                <table class="hlavicka-zaklad">
                    <tbody><tr class="first odd">
                        <th style="width: 50px" class="first">Soutěž:</th>
                        <td style="width: 200px">
                           23  M-2/C 
                        </td>
                        <td style="width: 20px"></td>
                        <th style="width: 100px">Kolo:</th>
                        <td style="width: 100px" class="last">
                         1 </td>
                    </tr>
                    <tr>
                        <th class="first">Číslo:</th>
                        <td>
                           A4C</td>
                        <td></td>
                        <th>Ćíslo utkání:</th>
                        <td class="last">
                           2022110A4C0104</td>
                    </tr>
                    <tr class="last odd">
                        <th class="first">Ročník:</th>
                        <td>
                             2022</td>
                        <td></td>
                        <th>Den:</th>
                        <td class="last">
                         20.08.2022 10:15</td>
                    </tr>
                </tbody></table>
                </div>
            </td>
        </tr>
    </tbody></table>
         <table class="vysledky">
        <tbody><tr class="first odd">
            <td class="hl1 first" colspan="3">Domácí <b>1090041 - Tělovýchovná jednota Kyje Praha 14   "B"</b></td>
            <td class="hl1 last" colspan="3">Hosté <b>1010041 - AFK SLAVIA MALEŠICE</b></td>
        </tr>
        <tr>
            <td class="w1 first">R</td>
            <td>RŮŽIČKA Milan</td>            
            <td class="clenid">68100467</td>
            <td colspan="2" class="last"><span class="label">Stadion:</span> KYJE  UMT.</td>
            
        </tr>

        <tr class="odd">
            <td class="w1 first">AR1</td>
            <td>ŠENFELD Jaroslav (N)</td>            
            <td class="clenid">77011026</td>
            
            <td>
                <span class="label">Výsledek utkání:</span><span class="vysledek-utkani"> 0:5
                    <span style="font-weight:normal;font-size:12px;padding-left:10px" class="penalta ">(PK:0:0)</span>

                                                           </span>                
            </td>
            <td class="last">
                <span class="label">Poločas utkání:</span><span class="vysledek-utkani"> 0:1</span>
            </td>
            
        </tr>

        <tr>
            <td class="w1 first">AR2</td>
            <td>VEČEŘA Petr (N)</td>
            
            <td class="clenid">79100683</td>
            <td colspan="2" class="last">
                <span class="label ">Diváků:</span>   20
            </td>
           
        </tr>

        <tr class="odd">
            <td class="w1 first">4R</td>
            <td>4Rj</td>            
            <td class="clenid">4Rc</td>

            <td><span class="label">Doba hry:</span>45+1 ; 45+1</td>
            <td class="last"><span class="label">Povrch hr. pl.:</span>Tráva</td>
          

          
        </tr>

        <tr>
            <td class="w1 first">DFA</td>
            <td>DFAj</td>
            
            <td class="clenid">DFAc</td>
           <td colspan="2" class="last">
                <span class="label ">Zápis vložil:</span> Růžička Milan (68100467)
            </td>
        </tr>

        <tr class="last odd">
            <td class="first">TD</td>
            <td>TDj</td>
            <td class="clenid">TDc</td>
            <td colspan="2" class="last">
                
                 RA:
                 <span style="padding-left:5px"></span>
                <span> ()</span>
           </td>
        
        </tr>


        
    </tbody></table>

          

    <table class="vysledky hraci">
        <tbody><tr class="first last odd">
            <td class="hl1 first" colspan="3">
                <h2>Hráči domácí</h2>       
                <table>
                    <tbody><tr class="first odd">
                                <th style="width: 15px" class="center first">Č.</th>
                                <th style="width: 230px">Příjmení a jméno</th>
                                <th style="" class="center">ID</th>
                                <th style="width: 50px" class="center" colspan="2">Stř.</th>
                                <th style="width: 25px" class="center" colspan="2">ŽK</th>
                                <th style="width: 25px" class="center">ČK</th>
                                <th style="width: 25px" class="center last">Br.</th>
                    </tr>
                    
                          <tr class="po1 kapitanFalse">
                             <td class="center first" style="width: 10px">1</td>
                             <td>
                                 <div>
                                 Benda Filip   
                                 <span style="float:right">B</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">91051991</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po2 kapitanFalse odd">
                             <td class="center first" style="width: 10px">10</td>
                             <td>
                                 <div>
                                 Bartakovič Jan   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">89042401</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po3 kapitanFalse">
                             <td class="center first" style="width: 10px">4</td>
                             <td>
                                 <div>
                                 Drahota Štěpán   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">81071745</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po4 kapitanFalse odd">
                             <td class="center first" style="width: 10px">9</td>
                             <td>
                                 <div>
                                 Broum Jiří   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">82121306</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po5 kapitanFalse">
                             <td class="center first" style="width: 10px">5</td>
                             <td>
                                 <div>
                                 Karpíšek Jakub   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">03110085</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po6 kapitanFalse odd">
                             <td class="center first" style="width: 10px">3</td>
                             <td>
                                 <div>
                                 Poborský František   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">05120034</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po7 kapitanFalse">
                             <td class="center first" style="width: 10px">7</td>
                             <td>
                                 <div>
                                 Shandra Yaroslav   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">93102242</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po8 kapitanTrue odd">
                             <td class="center first" style="width: 10px">8</td>
                             <td>
                                 <div>
                                 Tipta Miroslav <span class="kapitan">(K)</span>  
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">79011367</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po9 kapitanFalse">
                             <td class="center first" style="width: 10px">16</td>
                             <td>
                                 <div>
                                 Trinkmoc Miloš   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">73071087</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po10 kapitanFalse odd">
                             <td class="center first" style="width: 10px">2</td>
                             <td>
                                 <div>
                                 Poborský Karel   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">77080248</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po11 kapitanFalse">
                             <td class="center first" style="width: 10px">11</td>
                             <td>
                                 <div>
                                 Zeman Dominik   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">87080647</td>

                             <td class="center" style="width: 25px;text-align:center;">11</td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po12 kapitanFalse odd">
                             <td class="center first" style="width: 10px">6</td>
                             <td>
                                 <div>
                                 Jaroš Jakub   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">89072441</td>

                             <td class="center" style="width: 25px;text-align:center;">11</td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;">36</td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="po13 kapitanFalse last">
                             <td class="center first" style="width: 10px">31</td>
                             <td>
                                 <div>
                                 Šenfeld Jaroslav   
                                 <span style="float:right">N</span>
                                    <div style="clear:both;"></div>
                                 </div>
                                
                             </td>
                             <td class="center" style="width: 90px">77011026</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                </tbody></table>

            </td>
            <td class="hl1 last" colspan="3">
                <h2>Hráči hosté</h2>   
                <table>
                    <tbody><tr class="first odd">
                                <th style="width: 15px" class="center first">Č.</th>
                                <th style="width: 230px">Příjmení a jméno</th>
                                <th style="" class="center">ID</th>
                                <th class="center" colspan="2">Stř.</th>
                                <th class="center" colspan="2">ŽK</th>
                                <th style="width: 25px" class="center">ČK</th>
                                <th style="width: 25px" class="center last">Br.</th>
                    </tr>
                      
                         <tr class="po1 kapitanTrue">
                             <td class="center first">1</td>
                            <td>
                                 <div>
                                 Levý David  <span class="kapitan">(K)</span>  
                                 <span style="float:right">B</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">85031181</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po2 kapitanFalse odd">
                             <td class="center first">2</td>
                            <td>
                                 <div>
                                 Sládek Petr    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">91050347</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po3 kapitanFalse">
                             <td class="center first">3</td>
                            <td>
                                 <div>
                                 Florián Petr    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">94081594</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po4 kapitanFalse odd">
                             <td class="center first">4</td>
                            <td>
                                 <div>
                                 Jareš Roman    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">73080968</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po5 kapitanFalse">
                             <td class="center first">5</td>
                            <td>
                                 <div>
                                 Remiš Jakub    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">98120517</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po6 kapitanFalse odd">
                             <td class="center first">6</td>
                            <td>
                                 <div>
                                 Jasanský Jakub    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">95090991</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po7 kapitanFalse">
                             <td class="center first">7</td>
                            <td>
                                 <div>
                                 Desyk Oleksandr    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">88112124</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;">28</td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po8 kapitanFalse odd">
                             <td class="center first">8</td>
                            <td>
                                 <div>
                                 Hottek Jakub    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">83061562</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po9 kapitanFalse">
                             <td class="center first">14</td>
                            <td>
                                 <div>
                                 Vyhnal Pavel    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">90051895</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po10 kapitanFalse odd">
                             <td class="center first">11</td>
                            <td>
                                 <div>
                                 Bizhev Georgi    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">81061873</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;">4</td>
                         </tr>
                    
                         <tr class="po11 kapitanFalse">
                             <td class="center first">17</td>
                            <td>
                                 <div>
                                 Kundrát Tomáš    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">93011346</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;">1</td>
                         </tr>
                    
                         <tr class="po12 kapitanFalse odd">
                             <td class="center first">10</td>
                            <td>
                                 <div>
                                 Hons Pavel    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">69070349</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po13 kapitanFalse">
                             <td class="center first">12</td>
                            <td>
                                 <div>
                                 Dudys Oleg    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">88092288</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po14 kapitanFalse odd">
                             <td class="center first">9</td>
                            <td>
                                 <div>
                                 Liakhovets Oleh    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">95021868</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po15 kapitanFalse">
                             <td class="center first">13</td>
                            <td>
                                 <div>
                                 Bartoš Michael    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">77080655</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po16 kapitanFalse odd">
                             <td class="center first">16</td>
                            <td>
                                 <div>
                                 Blažej Jiří    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">90112280</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po17 kapitanFalse">
                             <td class="center first">15</td>
                            <td>
                                 <div>
                                 Burian Lukáš    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">87071035</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                         <tr class="po18 kapitanFalse last odd">
                             <td class="center first">18</td>
                            <td>
                                 <div>
                                 Joneš Petr    
                                 <span style="float:right">N</span>
                                      <div style="clear:both;"></div>
                                 </div>
                             </td>
                             <td class="center">90112142</td>

                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center" style="width: 25px;text-align:center;"></td>
                             <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                      </tbody></table>
            </td>
        </tr>
     </tbody></table>
   


     <table class="vysledky hraci">
        <tbody><tr class="first last odd">
            <td class="hl1 first" colspan="3">
                <h2>Funkcionáři a pořadatelé domácí</h2>       
                <table style="width:100%">
                    <tbody><tr class="first odd">
                        <th style="width: 110px" class="center first">Funkce</th>
                        <th class="center">Příjmení a jméno</th>
                        <th style="" class="center">ID</th>
                         <th style="" colspan="2" class="center last">ŽK</th>
                    </tr>
                    
                          <tr>
                             <td class="first">Hlavní pořadatel</td>
                             <td class="center">Chadima Václav</td>
                              <td class="center" style="width: 90px">54030121</td>
                              <td class="center" style="width: 25px;text-align:center;"></td>
                              <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                          <tr class="last odd">
                             <td class="first">Vedoucí</td>
                             <td class="center">Stejskal Pavel</td>
                              <td class="center" style="width: 90px">77121529</td>
                              <td class="center" style="width: 25px;text-align:center;"></td>
                              <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                </tbody></table>

            </td>
            <td class="hl1 last" colspan="3">
                <h2>Funkcionáři a pořadatelé hosté</h2>   
                 <table style="width:100%">
                    <tbody><tr class="first odd">
                        <th style="width: 100px" class="center first">Funkce</th>
                        <th class="center">Příjmení a jméno</th>
                        <th style="" class="center">ID</th>
                        <th style="" colspan="2" class="center last">ŽK</th>
                    </tr>
                      
                        <tr>
                             <td class="first">Vedoucí</td>
                             <td class="center">Hottek Luděk</td>
                              <td class="center" style="width: 90px">58080258</td>
                              <td class="center" style="width: 25px;text-align:center;"></td>
                              <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                        <tr class="odd">
                             <td class="first">Trenér</td>
                             <td class="center">Hons Pavel</td>
                              <td class="center" style="width: 90px">69070349</td>
                              <td class="center" style="width: 25px;text-align:center;"></td>
                              <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                        <tr class="last">
                             <td class="first">Asistent 1</td>
                             <td class="center">Večeřa Aleš</td>
                              <td class="center" style="width: 90px">68050831</td>
                              <td class="center" style="width: 25px;text-align:center;"></td>
                              <td class="center last" style="width: 25px;text-align:center;"></td>
                         </tr>
                    
                      </tbody></table>
            </td>
        </tr>
     </tbody></table>


      
   


     <table class="vysledky hraci">
        <tbody><tr class="first last odd">
            <td class="hl1 first" colspan="3">
                <h2>Osobní tresty domácí</h2>       
              <table style="width:100%">
                    <tbody><tr class="first last odd">
                                <th class="first">Příjmení a jméno</th>
                                <th style="width: 80px" class="center">ID</th>
                                <th style="width: 50px" class="center last">Minuta</th>
                    </tr>
                   
                    


                     

                </tbody></table>

            </td>
            <td class="hl1 last" colspan="3">
                <h2>Osobní tresty hosté</h2>   
               <table style="width:100%">
                    <tbody><tr class="first last odd">
                                <th class="first">Příjmení a jméno</th>
                                <th style="width: 80px" class="center">ID</th>
                                <th style="width: 50px" class="center last">Minuta</th>
                    </tr>
                   
                    


                    

                </tbody></table>
            </td>
        </tr>
     </tbody></table>


    <table class="vysledky hraci">
        <tbody><tr class="first last odd">
            <td class="hl1 first" colspan="3">
                <h2>Střelci domácí</h2>       
                  <table style="width:100%">
                    <tbody><tr class="first last odd">
                                <th style="width: 20px" class="center first">P.</th>
                                <th>Příjmení a jméno</th>
                                <th style="width: 80px" class="center">Typ</th>        
                                <th class="center" style="width: 50px">ID</th>
                                <th style="width: 50px" class="center last">Minuta</th>
                    </tr>
                    
                </tbody></table>
            </td>
            <td class="hl1 last" colspan="3">
                <h2>Střelci hosté</h2>   
                 <table style="width:100%">
                    <tbody><tr class="first odd">
                                <th style="width: 20px" class="center first">P.</th>
                                <th>Příjmení a jméno</th>
                                <th style="width: 80px" class="center">Typ</th>        
                                <th class="center" style="width: 50px">ID</th>                          
                        <th class="center last" style="width: 50px">Minuta</th>
                    </tr>
                    
                          <tr>
                             <td class="center first" style="width: 10px">1</td>
                             <td>Bizhev Georgi
                              
                             </td>
                              <td>Branka</td>
                             <td class="center" style="width: 70px">81061873</td>                              
                             <td class="center last" style="width: 25px">57</td>
                         </tr>
                    
                          <tr class="odd">
                             <td class="center first" style="width: 10px">2</td>
                             <td>Bizhev Georgi
                              
                             </td>
                              <td>Branka</td>
                             <td class="center" style="width: 70px">81061873</td>                              
                             <td class="center last" style="width: 25px">63</td>
                         </tr>
                    
                          <tr>
                             <td class="center first" style="width: 10px">3</td>
                             <td>Bizhev Georgi
                              
                             </td>
                              <td>Branka</td>
                             <td class="center" style="width: 70px">81061873</td>                              
                             <td class="center last" style="width: 25px">71</td>
                         </tr>
                    
                          <tr class="odd">
                             <td class="center first" style="width: 10px">4</td>
                             <td>Bizhev Georgi
                              
                             </td>
                              <td>Branka</td>
                             <td class="center" style="width: 70px">81061873</td>                              
                             <td class="center last" style="width: 25px">35</td>
                         </tr>
                    
                          <tr class="last">
                             <td class="center first" style="width: 10px">5</td>
                             <td>Kundrát Tomáš
                              
                             </td>
                              <td>Branka</td>
                             <td class="center" style="width: 70px">93011346</td>                              
                             <td class="center last" style="width: 25px">60</td>
                         </tr>
                    
                </tbody></table>
            </td>
        </tr>
     </tbody></table>

    
    
    
</div>


    

   

    </div>
    
<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="8293F410">
</div></form>


</body></html>
"""


def get_code(sitekey: str, url: str) -> dict:
    """
    Funkce ziska capcha kod ze zadaneho url s capchou

    Priklad vystupu:

    {'CapchaId': '71914160706', 'code': '03A...75w'}

    :param sitekey: "sitekey z html kodu"
    :param url: "url s capchou"
    :return: {slovnik s kodem}
    """
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', '6a9f5831289bfb362b04f134cbd24fd0')
    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)
    except Exception as e:
        print(e)
    else:
        return result


def capcha_solver(browser: webdriver, sitekey: str, url: str) -> None:
    """
    Funkce pouzije ziskany capcha kod, vlozi ho do html kodu a klikne na tl. Pokracovat.

    :param browser: webdriver
    :param sitekey: "sitekey z html kodu"
    :param url: "url s capchou"
    :return: None
    """
    token = get_code(sitekey, url)
    code = token['code']
    # print(code)

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "g-recaptcha-response"))
    )

    time.sleep(3)

    # Vlozeni code do HTML kodu
    browser.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'"
    )

    time.sleep(3)

    # Nalezeni a stisknuti tlacitka Pokracovat
    button_pokracovat = browser.find_element(By.CSS_SELECTOR, 'a[id="MainContent_btnLogin"]')
    button_pokracovat.click()

    time.sleep(2)


def stahni_html_kod(url_adresa: str) -> BeautifulSoup:
    """
    Funkce stahne html kod z webu. Vrati naparsovany kod, pripraveny k prohledavani.

    Beautifulsoup =
    <html><body>
    ... telo ...
    </body></html>

    :param url_adresa: "url_adresa"
    :return: objekt BeautifulSoup
    """
    print(f"Stahuji data z URL adresy: {url_adresa}")
    odpoved = requests.get(url_adresa)

    return BeautifulSoup(odpoved.text, "html.parser")


def stahni_html_kod_rucne(html_kod: str) -> BeautifulSoup:
    """
    Funkce prevede rucne stazeny html kod na naparsovany objekt Beautifulsoup, ve kterem uz je mozno vyhledavat.

    Beautifulsoup =
    <html><body>
    ... telo ...
    </body></html>

    :param html_kod: "html kod"
    :return: objekt BeautifulSoup
    """
    return BeautifulSoup(html_kod, "html.parser")


def naparsuj_html_kod_ze_stringu(html_kod: str) -> BeautifulSoup:
    """
    Funkce prevede html kod "str" na naparsovany objekt Beautifulsoup, ve kterem uz je mozno vyhledavat.

    Beautifulsoup =
    <html><body>
    ... telo ...
    </body></html>

    :param html_kod: "html kod"
    :return: objekt BeautifulSoup
    """
    return BeautifulSoup(html_kod, "html.parser")


def stahni_odkazy_na_zapisy():
    odkazy_na_zapisy = []
    bs_obj = stahni_html_kod_rucne(a)
    odkazy = bs_obj.find_all("td", {"class": "center last"}, limit=7)
    for odkaz in odkazy:
        odkazy_na_zapisy.append(odkaz.find("a").get("href"))
    print(odkazy_na_zapisy)


def stahni_zapis(html_kod_str: str):
    bs_obj = stahni_html_kod_rucne(html_kod_str)
    # print(bs_obj)
    hraci_domaci = bs_obj.find("td", {"class": "hl1 first"})
    # h = hraci_domaci.find_all("tr")
    print(hraci_domaci.text)


def temp_zkusebni_stazeni_zapisu(browser, url_prvni_zapis, url_druhy_zapis, url_treti_zapis):
    browser.get(url_prvni_zapis)
    html_1 = browser.page_source
    time.sleep(2)
    # print(html)
    # html je class str
    # print(type(html))
    stahni_zapis(html_1)

    browser.get(url_druhy_zapis)
    html_2 = browser.page_source
    time.sleep(2)
    # print(html)
    # html je class str
    # print(type(html))
    stahni_zapis(html_2)

    browser.get(url_treti_zapis)
    html_3 = browser.page_source
    time.sleep(2)
    # print(html)
    # html je class str
    # print(type(html))
    stahni_zapis(html_3)


def naparsuj_zapis(str_zapis):
    return naparsuj_html_kod_ze_stringu(str_zapis)


def stahni_hlavicku_zapisu(naparsovany_zapis):
    tabulka_hlavicka = naparsovany_zapis.tbody.tbody

    data_hlavicka_hlavicka = ["Soutěž", "Kolo", "Číslo", "Číslo utkání", "Ročník", "Den", "Čas"]
    soutez = tabulka_hlavicka.find("tr", {"class": "first odd"}).td.text.strip("\n ")
    kolo = tabulka_hlavicka.find("tr", {"class": "first odd"}).find("td", {"class": "last"}).text.strip("\n ")
    cislo = tabulka_hlavicka.tr.find_next_sibling().td.text.strip("\n ")
    cislo_utkani = tabulka_hlavicka.tr.find_next_sibling().find("td", {"class": "last"}).text.strip("\n ")
    rocnik = tabulka_hlavicka.find("tr", {"class": "last odd"}).td.text.strip("\n ")
    den_cas = tabulka_hlavicka.find("tr", {"class": "last odd"}).find("td", {"class": "last"}).text.strip("\n ")
    den, cas = den_cas.split()

    data_hlavicka_obsah = [soutez, kolo, cislo, cislo_utkani, rocnik, den, cas]

    # print([data_hlavicka_hlavicka, data_hlavicka_obsah])

    return [data_hlavicka_hlavicka, data_hlavicka_obsah]


def stahni_vysledky(naparsovany_zapis):
    tabulka_vysledky = naparsovany_zapis.find("table", {"class": "vysledky"})

    data_vysledky_hlavicka = [
        "Domácí - číslo", "Domácí - text", "Hosté - číslo", "Hosté - text", "R jméno", "R číslo", "AR1 jméno",
        "AR1 číslo", "AR2 jméno"#, "AR2 číslo", "4R jméno", "4R číslo", "DFA jméno", "DFA číslo", "TD jméno",
        #"TD číslo", "Stadion", "Výsledek utkání", "Poločas utkání", "Diváků", "Doba hry 1. poločas",
        #"Doba hry 2. poločas", "Povrch hr. pl.", "Zápis vložil", "RA"
    ]

    # TODO co je (N) u AR1 a AR2? Odstranit to?
    # Doplnit kolonku cislo u R, AR1 a AR2
    domaci_cislo_text = tabulka_vysledky.find("tr", {"class": "first odd"}).find("td", {"class": "hl1 first"}).b.text
    domaci_cislo, domaci_text = domaci_cislo_text.split("-")
    domaci_cislo = domaci_cislo.strip()
    domaci_text = domaci_text.strip()
    # Smaze mezery navic mezi nazvem tymu a "B"
    domaci_text = re.sub(r"\s{2,}", " ", domaci_text)
    hoste_cislo_text = tabulka_vysledky.find("tr", {"class": "first odd"}).find("td", {"class": "hl1 last"}).b.text
    hoste_cislo, hoste_text = hoste_cislo_text.split("-")
    hoste_cislo = hoste_cislo.strip()
    hoste_text = hoste_text.strip()
    # Smaze mezery navic mezi nazvem tymu a "B"
    hoste_text = re.sub(r"\s{2,}", " ", hoste_text)
    r_jmeno = tabulka_vysledky.tr.find_next_sibling().td.find_next_sibling().text
    r_cislo = tabulka_vysledky.tr.find_next_sibling().td.find_next_sibling().find_next_sibling().text
    ar1_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().td.find_next_sibling().text
    ar1_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().td.find_next_sibling()\
        .find_next_sibling().text
    ar2_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().td\
        .find_next_sibling().text
    ar2_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().td\
        .find_next_sibling().find_next_sibling().text
    # TODO smazat z html kodu R4j, R4c, DFAj, DFAc, TDj, TDc
    r4_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .td.find_next_sibling().text
    r4_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .td.find_next_sibling().find_next_sibling().text
    dfa_jmeno = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .find_next_sibling().td.find_next_sibling().text
    dfa_cislo = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .find_next_sibling().td.find_next_sibling().find_next_sibling().text
    td_jmeno = tabulka_vysledky.find("tr", {"class": "last odd"}).td.find_next_sibling().text
    td_cislo = tabulka_vysledky.find("tr", {"class": "last odd"}).td.find_next_sibling().find_next_sibling().text
    stadion = tabulka_vysledky.tr.find_next_sibling().find("td", {"class": "last"}).text.replace("Stadion: ", "")
    # TODO doladit pokutove kopy
    vysledek_utkani = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().td.find_next_sibling()\
        .find_next_sibling().find_next_sibling().find("span", {"class": "vysledek-utkani"}).text
    polocas_utkani = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find("td", {"class": "last"})\
        .find("span", {"class": "vysledek-utkani"}).text.strip("\n ")
    divaku = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().td.\
        find_next_sibling().find_next_sibling().find_next_sibling().text.strip("\n ").replace("Diváků: ", "")
    # Odstraneni prebytecnych mezer - odstrani jednu a vice mezer a nahradi ji zadnou mezerou
    divaku = re.sub(r"\s+", "", divaku)
    doba_hry_prvni_polocas, doba_hry_druhy_polocas = tabulka_vysledky.tr.find_next_sibling().find_next_sibling()\
        .find_next_sibling().find_next_sibling().td.find_next_sibling().find_next_sibling().find_next_sibling()\
        .text.replace("Doba hry:", "").split(";")
    doba_hry_prvni_polocas = doba_hry_prvni_polocas.strip()
    doba_hry_druhy_polocas = doba_hry_druhy_polocas.strip()
    povrch_hr_pl = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text\
        .replace("Povrch hr. pl.:", "")
    zapis_vlozil = tabulka_vysledky.tr.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()\
        .find_next_sibling().find("td", {"class": "last"}).text.replace("Zápis vložil: ", "").strip("\n ")
    # TODO co je RA a v jakém formátu to bude? Zatím tam jsou jen dvě závorky ()
    ra = tabulka_vysledky.find("tr", {"class": "last odd"}).find("td", {"class": "last"}).text\
        .replace("RA:", "").strip("\n ")

    data_vysledky_obsah = [
        domaci_cislo, domaci_text, hoste_cislo, hoste_text, r_jmeno, r_cislo, ar1_jmeno, ar1_cislo, ar2_jmeno#,
        #ar2_cislo, r4_jmeno, r4_cislo, dfa_jmeno, dfa_cislo, td_jmeno, td_cislo, stadion, vysledek_utkani,
        #polocas_utkani, divaku, doba_hry_prvni_polocas, doba_hry_druhy_polocas, povrch_hr_pl, zapis_vlozil, ra
    ]

    print([data_vysledky_hlavicka, data_vysledky_obsah])

    return [data_vysledky_hlavicka, data_vysledky_obsah]


def stahni_data_hracu(naparsovany_zapis, domaci_hoste):
    if domaci_hoste == "domaci":
        hraci = naparsovany_zapis.find("table", {"class": "vysledky hraci"}).tbody.tr.td.find_all("tr")
    elif domaci_hoste == "hoste":
        hraci = naparsovany_zapis.find("table", {"class": "vysledky hraci"}).tbody.tr.find("td", {"class": "hl1 last"})\
            .find_all("tr")

    hraci_statistika = []
    hraci_statistika_hlavicka = ["Číslo", "Příjmení a jméno", "Post", "ID", "Střídání", "-", "ŽK", "-", "ČK", "BR"]
    hraci_statistika.append(hraci_statistika_hlavicka)

    # Stazeni dat jednoho hrace
    for hrac in hraci:
        jeden_hrac_statistika = []
        zapis_do_statistik = False
        tds = hrac.find_all("td")
        for idx, td in enumerate(tds, start=1):
            if idx == 2:
                temp = td.text.strip().split("\n")
                temp[0] = temp[0].strip()
                temp[1] = temp[1].strip()
                jeden_hrac_statistika.extend(temp)
            else:
                jeden_hrac_statistika.append(td.text)
            zapis_do_statistik = True

        if zapis_do_statistik:
            hraci_statistika.append(jeden_hrac_statistika)
    # print(hraci_statistika)

    return hraci_statistika


def vygeneruj_csv_soubor(nazev_csv_souboru: str, data_pro_csv_tabulku: list[list]) -> None:
    """
    Funkce vytvori .csv soubor.

    :param nazev_csv_souboru: "nazev_csv_souboru.csv"
    :param data_pro_csv_tabulku: [[], [], [], [], ...]
    :return: None
    """
    print(f"Ukladam stazena data do souboru: {nazev_csv_souboru}")
    # Nastaveni oddelovace na středník
    csv.register_dialect('myDialect', delimiter=';', quoting=csv.QUOTE_NONE)
    # Nachystani noveho souboru na zapis
    nove_csv = open(nazev_csv_souboru, mode="w", newline='', encoding='utf-8')
    # Vytvoreni noveho csv souboru
    zapisovac = csv.writer(nove_csv, dialect='myDialect')
    # Zaspis stazenych dat do csv souboru
    for idx in range(len(data_pro_csv_tabulku)):
        zapisovac.writerow(data_pro_csv_tabulku[idx])
    # Uzavreni csv souboru
    nove_csv.close()


def main():
    sitekey = "6LdleRoUAAAAAFPzy5u9zlmtLy4qKT_Jb8EItoad"
    url = "https://is.fotbal.cz/security-valid.aspx?hidemenu=1&ret=%2fzapasy%2fzapis-o-utkani-report.aspx%3fzapas%3d18c8bd4f-cff6-40be-a67a-c30428d3e027%26zapis%3d1%26noprint%3d1%26btnprint%3d1%26.htm"
    prvni_cast_url = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=cb0b2f5b-07ac-4d51-8064-64336b349e40&zapis=1&noprint=1&btnprint=1&.htm"
    url_soutez = "https://is.fotbal.cz/souteze/detail-souteze.aspx?req=ae9809e0-5712-4abd-b99a-997cf9d3d8c6&fbclid=IwAR3NizZ2RB1Ffj8fObluwhR9wlFEeCYRB7ihXm8mCwy308cDMMzQMfMKuaU"

    url_prvni_zapis = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=cb0b2f5b-07ac-4d51-8064-64336b349e40&zapis=1&noprint=1&btnprint=1&.htm"
    url_druhy_zapis = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=2427a903-53a5-4b1b-b245-e53521038f7d&zapis=1&noprint=1&btnprint=1&.htm"
    url_treti_zapis = "https://is.fotbal.cz/zapasy/zapis-o-utkani-report.aspx?zapas=a31f61d1-53c0-4daf-9121-765a1e6ad2ee&zapis=1&noprint=1&btnprint=1&.htm"

    # Pouze otevreni prohlizece Chrome (bez nacteni webove stranky)
    # browser = webdriver.Chrome()
    # browser.get(url)
    # browser.get(url_soutez)
    # html = browser.page_source
    # time.sleep(2)
    # print(html)

    # capcha_solver(browser, sitekey, url)

    # stahni_odkazy_na_zapisy()

    # bs_obj = stahni_html_kod(prvni_cast_url)
    # print(bs_obj)

    # temp_zkusebni_stazeni_zapisu(browser, url_prvni_zapis, url_druhy_zapis, url_treti_zapis)

    naparsovany_zapis = naparsuj_zapis(prvni_zapis)

    data_hlavicka_zapisu = stahni_hlavicku_zapisu(naparsovany_zapis)
    data_vysledky = stahni_vysledky(naparsovany_zapis)
    # data_hraci_domaci = stahni_data_hracu(naparsovany_zapis, "domaci")
    # data_hraci_hoste = stahni_data_hracu(naparsovany_zapis, "hoste")

    vygeneruj_csv_soubor("data_hlavicka_zapisu.csv", data_hlavicka_zapisu)
    vygeneruj_csv_soubor("data_vysledky.csv", data_vysledky)
    # vygeneruj_csv_soubor("data_hraci_domaci.csv", data_hraci_domaci)
    # vygeneruj_csv_soubor("data_hraci_hoste.csv", data_hraci_hoste)

    # Cas, po ktery zustane prohlizec otevreny po vsech akcich
    # time.sleep(1000)


if __name__ == "__main__":
    main()