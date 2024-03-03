from konlpy.tag import Hannanum
from collections import Counter
import csv

#filename = "\\secu.txt"
#f=open(filename,'r',encoding='utf-8')
#news = f.read()


hannanum = Hannanum()
news="면리제(Myeon-rije)는 조선 시대 고을의 영역을 면(面)과 리(里)로 세분하여 편제한 행정 제도입니다. 이는 지방 지배를 강화하기 위해 실시된 제도로, 자연촌의 성장을 바탕으로 오가작통제(五家作統制)를 포함하여 실질적으로 정착되었습니다. 면리제는 군현제와 함께 고려 시대 이래 잔존했던 속현(屬縣)과 임내(任內) 등을 정리하고 국가의 지방 지배력을 촌락까지 확대하기 위해 조선왕조에 의해 제정되었습니다. 면리제는 조선 전기에 시작되어 조선 후기에 정착되었습니다. 면리제의 정착에는 시간이 걸렸으며, 양란 이후 숙종 때에 오가작통 제도가 시행되면서 면리제가 실질화되었습니다. 이를 통해 국가의 대민 지배력이 한층 강화되었습니다. 면리제는 조선 왕조가 군현제를 시행하고 지방 지배력을 강화하려는 노력의 일환으로, 자연촌의 성장을 바탕으로 오가작통제를 포함하여 제정되었습니다. 이를 통해 속현과 임내 등 기존의 행정 제도를 정리하고 지방 통치를 강화하였습니다. 면리제에 대한 기록으로는 『경국대전(經國大典)』의 호전(戶典)과 호적(戶籍)에 언급된 내용들이 있습니다. 이 기록들은 면리제의 행정 세부 사항과 편제 방식을 담고 있을 것으로 추정됩니다."

ttt = hannanum.nouns(news)
print(ttt)

for i,v in enumerate(ttt):
  if len(v)<2:
    ttt.pop(i)

print(ttt)

counte = Counter(ttt)
#f.close()


noun_list = counte.most_common(10)

print(noun_list)

for v in noun_list:
  print(v)


# save in txt file
with open("noun_list.txt", 'w', encoding='utf-8') as f:
  for v in noun_list:
      f.write(" ".join(map(str,v)))
      f.write("\n")

# save in csv file
with open("noun_list.csv", 'w', newline='', encoding='euc-kr') as f:
  csvw=csv.writer(f)
  for v in noun_list:
      csvw.writerow(v)
