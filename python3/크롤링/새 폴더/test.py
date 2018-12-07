text = '''<div id=""wrap"">
<div id=""da_base""></div>
<div id=""da_stake""></div>
<div id=""header"">
<!-- Skip navigation -->
<div id=""u_skip"">
<a href=""#lnb"" tabindex=""1""><span>메인 메뉴로 바로가기</span></a>
<a href=""#snb"" tabindex=""2""><span>서브 메뉴로 바로가기</span></a>
<a href=""#main_content"" tabindex=""3""><span>본문으로 바로가기</span></a>
</div>
<!-- //Skip navigation -->
<div class=""snb_area"">
<div class=""snb_inner"">
<div class=""gnb_wrap"">
<!-- GNB 마크업 -->
<div id=""gnb""></div>
<!-- //GNB 마크업 -->
</div>
<div id=""snb_wrap"">
<h1><a class=""h_logo nclicks(STA.naver)"" href=""http://www.naver.com/""><span class=""blind"">NAVER</span></a>
<a class=""h_news nclicks(STA.news)"" href=""http://news.naver.com/""><span class=""blind"">뉴스</span></a> </h1>
<ul class=""snb_related_service"">
<li><span class=""snb_bdr""></span><a class=""nclicks(STA.enter)"" href=""http://entertain.naver.com/home""><img alt=""TV연예"" height=""19"" src=""http://static.news.naver.net/image/news/2017/10/snb_h_entertain.png"" width=""52""/></a></li>
<li><span class=""snb_bdr""></span><a class=""nclicks(STA.sports)"" href=""http://sports.news.naver.com""><img alt=""스포츠"" height=""19"" src=""http://static.news.naver.net/image/news/2017/10/snb_h_sports.png"" width=""48""/></a></li>
<li><span class=""snb_bdr""></span><a class=""nclicks(STA.newsstand)"" href=""http://newsstand.naver.com""><img alt=""뉴스스탠드"" height=""19"" src=""http://static.news.naver.net/image/news/2017/10/snb_h_newsstand.png"" width=""77""/></a></li>
<li><span class=""snb_bdr""></span><a class=""nclicks(STA.weather)"" href=""http://weather.naver.com""><img alt=""날씨"" height=""19"" src=""http://static.news.naver.net/image/news/2017/10/snb_h_weather.png"" width=""31""/></a></li>
</ul>
</div>
</div>
</div>
<div class=""lnb_area"">
<div class=""lnb_inner"">
<div class=""lnb_menu"" id=""lnb"">'''

import re

joosuk = re.compile(r'^(<!--).*(-->)$')
open_tag = re.compile(r'^<div.*?>$')
close_tag = re.compile(r'^</.*>$')

text = re.sub('<.+?>', '', text, 0, re.I|re.S)
print(text)


how_cut = 2
real_cut = how_cut+1
liste = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(len(liste)-1, len(liste)-real_cut, -1):
    del (liste[i])

print(liste)
