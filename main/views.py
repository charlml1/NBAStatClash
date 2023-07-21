from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from .forms import PlayerForm, PointsForm

# Create your views here.

def home(response):
	return render(response, "main/home.html", {})

def categories(response):
	if response.method == "POST":
		# print(response.POST)
		form = PlayerForm(response.POST)
		player1=Player.objects.filter(name=response.POST.get("player1"), year=2023)[0]
		player2=Player.objects.filter(name=response.POST.get("player2"), year=2023)[0]
		
		# fg%, 3p%, 2p%, efg%, ft% 
		name = player1.name
		team = player1.team
		pos = player1.position
		age = player1.age
		pts = player1.pts
		reb = player1.reb
		ast = player1.ast
		stl = player1.stl
		blk = player1.blk
		fg = player1.fgpercent
		ft = player1.ftpercent
		threepm = player1.threepm
		gp = player1.gamesPlayed
		gs = player1.gamesStarted
		turnover = player1.tov
		threePointPer = player1.threeppercent

		if fg == "":
			fg = "0"
		if ft == "":
			ft = "0"
		if threePointPer == "":
			threePointPer = "0"

		fg = str(round(float(fg)*100, 1))
		ft = str(round(float(ft)*100, 1))
		threePointPer = str(round(float(threePointPer)*100, 1))

		name2 = player2.name
		team2 = player2.team
		pos2 = player2.position
		age2 = player2.age
		pts2 = player2.pts
		reb2 = player2.reb
		ast2 = player2.ast
		stl2 = player2.stl
		blk2 = player2.blk
		fg2 = player2.fgpercent
		ft2 = player2.ftpercent
		threepm2 = player2.threepm
		gp2 = player2.gamesPlayed
		gs2 = player2.gamesStarted
		turnover2 = player2.tov
		threePointPer2 = player2.threeppercent

		if fg2 == "":
			fg2 = "0"
		if ft2 == "":
			ft2 = "0"
		if threePointPer2 == "":
			threePointPer2 = "0"

		fg2 = str(round(float(fg2)*100, 1))
		ft2 = str(round(float(ft2)*100, 1))
		threePointPer2 = str(round(float(threePointPer2)*100, 1))

		CENTER = 47
		info = "{}".format(name).center(34, " ") + "\t\t"
		info += "{}".format(name2).center(32, " ") + "\n"
		info += "Team: {}, Position: {}, Age: {}".format(team, pos, age).ljust(CENTER, " ")
		info += "Team: {}, Position: {}, Age: {}".format(team2, pos2, age2) + "\n"
		info += "{}/{}/{}  {} TOs".format(pts, reb, ast, turnover).ljust(CENTER, " ")
		info += "{}/{}/{}  {} TOs".format(pts2, reb2, ast2, turnover2) + "\n"
		info += "{} STL {} BLK".format(stl, blk).ljust(CENTER, " ")
		info += "{} STL {} BLK".format(stl2, blk2) + "\n"
		info += "{} FG% {} 3P% {} FT%".format(fg, threePointPer, ft).ljust(CENTER, " ")
		info += "{} FG% {} 3P% {} FT%".format(fg2, threePointPer2, ft2) + "\n"
		info += "{} 3PM  {} Games Played  {} Games Started".format(threepm, gp, gs).ljust(CENTER, " ")
		info += "{} 3PM  {} Games Played  {} Games Started".format(threepm2, gp2, gs2) + "\n"

		# \t\t\t\t{}/{}/{}  {} TOs\n\t\t\t\t\t".format(
  #           ,) + "{} STL {} BLK\n\t\t\t{} FG% {} 3P% {} FT%\n.format(
  #           stl2, blk2, , fg2, threePointPer2, ft2, ,) + "\t{} 3PM  {} Games Played  {} Games Started".format(gs, threepm2, gp2, gs2)

		COMPARISON_SPACE = 84
		info += "_"*87 + "\n" + "COMPARISON".center(COMPARISON_SPACE, " ") + "\n"

		# fg%
		fgDiff = abs(float(fg) - float(fg2))
		fgWinner = "Tied"
		if fg > fg2:
			fgWinner = name
		if fg < fg2:
			fgWinner = name2
		info += "+ {:.1f} Field Goal % ({})".format(fgDiff, fgWinner).center(COMPARISON_SPACE, " ") + "\n"

		# ft%
		ftDiff = abs(float(ft) - float(ft2))
		ftWinner = "Tied"
		if ft > ft2:
			ftWinner = name
		if ft < ft2:
			ftWinner = name2
		info += "+ {:.1f} Free Throw % ({})".format(ftDiff, ftWinner).center(COMPARISON_SPACE, " ") + "\n"

		# 3pm
		threepmDiff = abs(float(threepm) - float(threepm2))
		threepmWinner = "Tied"
		if threepm > threepm2:
		    threepmWinner = name
		if threepm < threepm2:
		    threepmWinner = name2
		info += "  + {:.1f} 3 Pointers Made ({})".format(threepmDiff, threepmWinner).center(COMPARISON_SPACE, " ") + "\n"

		# pts
		ptsDiff = abs(float(pts) - float(pts2))
		ptsWinner = "Tied"
		if pts > pts2:
		    ptsWinner = name
		if pts < pts2:
		    ptsWinner = name2
		info += "  + {:.1f} Points ({})".format(ptsDiff, ptsWinner).center(COMPARISON_SPACE, " ") + "\n"

		# reb
		rebDiff = abs(float(reb) - float(reb2))
		rebWinner = "Tied"
		if reb > reb2:
		    rebWinner = name
		if reb < reb2:
		    rebWinner = name2
		info += "  + {:.1f} Rebounds ({})".format(rebDiff, rebWinner).center(COMPARISON_SPACE, " ") + "\n"

		# ast
		astDiff = abs(float(ast) - float(ast2))
		astWinner = "Tied"
		if ast > ast2:
		    astWinner = name
		if ast < ast2:
		    astWinner = name2
		info += "  + {:.1f} Assists ({})".format(astDiff, astWinner).center(COMPARISON_SPACE, " ") + "\n"

		# stl
		stlDiff = abs(float(stl) - float(stl2))
		stlWinner = "Tied"
		if stl > stl2:
		    stlWinner = name
		if stl < stl2:
		    stlWinner = name2
		info += "  + {:.1f} Steals ({})".format(stlDiff, stlWinner).center(COMPARISON_SPACE, " ") + "\n"

		# blk
		blkDiff = abs(float(blk) - float(blk2))
		blkWinner = "Tied"
		if blk > blk2:
		    blkWinner = name
		if blk < blk2:
		    blkWinner = name2
		info += "  + {:.1f} Blocks ({})".format(blkDiff, blkWinner).center(COMPARISON_SPACE, " ") + "\n"

		# tov
		turnoverDiff = abs(float(turnover) - float(turnover2))
		turnoverWinner = "Tied"
		if turnover < turnover2:
		    turnoverWinner = name
		if turnover > turnover2:
		    turnoverWinner = name2
		info += "  - {:.1f} TOV ({})".format(turnoverDiff, turnoverWinner).center(COMPARISON_SPACE, " ") + "\n"

		# games played
		gpDiff = abs(int(gp) - int(gp2))
		# print("name: {}, name2, {}, gp: {}, gp2: {}".format(name, name2, gp, gp2))
		gpWinner = name
		gpLoser = name2
		# print("gpWinner: {}, gpLoser, {}, gp: {}, gp2: {}".format(gpWinner, gpLoser, gp, gp2))
		# print(type(gp2))
		# print(gp)
		# print(gp2 > gp)
		if int(gp2) > int(gp):
		    gpWinner = name2
		    gpLoser = name
		# print("gpWinner: {}, gpLoser, {}, gp: {}, gp2: {}".format(gpWinner, gpLoser, gp, gp2))
		info += "{} played {} more games than {}".format(gpWinner, gpDiff, gpLoser).center(COMPARISON_SPACE, " ") + "\n"

		# games started
		gsDiff = abs(int(gs) - int(gs2))
		gsWinner = name
		gsLoser = name2
		if int(gs2) > int(gs):
		    gsWinner = name2
		    gsLoser = name
		info += "{} started {} more games than {}".format(gsWinner, gsDiff, gsLoser).center(COMPARISON_SPACE, " ") + "\n"

		return render(response, "main/categories.html", {"form":form, "info":info})

	# playerList = Player.objects.all()
	form = PlayerForm()
	info = ""
	return render(response, "main/categories.html", {"form":form, "info":info})

def points(response):
	if response.method == "POST":
		# Comparing the two players' reg season stats
		playerForm = PlayerForm(response.POST)
		pointsForm = PointsForm(response.POST)
		player1=Player.objects.filter(name=response.POST.get("player1"), year=2023)[0]
		player2=Player.objects.filter(name=response.POST.get("player2"), year=2023)[0]
		
		# fg%, 3p%, 2p%, efg%, ft% 
		name = player1.name
		team = player1.team
		pos = player1.position
		age = player1.age
		pts = player1.pts
		reb = player1.reb
		ast = player1.ast
		stl = player1.stl
		blk = player1.blk
		fg = player1.fgpercent
		ft = player1.ftpercent
		threepm = player1.threepm
		gp = player1.gamesPlayed
		gs = player1.gamesStarted
		turnover = player1.tov
		threePointPer = player1.threeppercent

		if fg == "":
			fg = "0"
		if ft == "":
			ft = "0"
		if threePointPer == "":
			threePointPer = "0"

		fg = str(round(float(fg)*100, 1))
		ft = str(round(float(ft)*100, 1))
		threePointPer = str(round(float(threePointPer)*100, 1))

		name2 = player2.name
		team2 = player2.team
		pos2 = player2.position
		age2 = player2.age
		pts2 = player2.pts
		reb2 = player2.reb
		ast2 = player2.ast
		stl2 = player2.stl
		blk2 = player2.blk
		fg2 = player2.fgpercent
		ft2 = player2.ftpercent
		threepm2 = player2.threepm
		gp2 = player2.gamesPlayed
		gs2 = player2.gamesStarted
		turnover2 = player2.tov
		threePointPer2 = player2.threeppercent

		if fg2 == "":
			fg2 = "0"
		if ft2 == "":
			ft2 = "0"
		if threePointPer2 == "":
			threePointPer2 = "0"

		fg2 = str(round(float(fg2)*100, 1))
		ft2 = str(round(float(ft2)*100, 1))
		threePointPer2 = str(round(float(threePointPer2)*100, 1))

		CENTER = 47
		info = "{}".format(name).center(34, " ") + "\t\t"
		info += "{}".format(name2).center(32, " ") + "\n"
		info += "Team: {}, Position: {}, Age: {}".format(team, pos, age).ljust(CENTER, " ")
		info += "Team: {}, Position: {}, Age: {}".format(team2, pos2, age2) + "\n"
		info += "{}/{}/{}  {} TOs".format(pts, reb, ast, turnover).ljust(CENTER, " ")
		info += "{}/{}/{}  {} TOs".format(pts2, reb2, ast2, turnover2) + "\n"
		info += "{} STL {} BLK".format(stl, blk).ljust(CENTER, " ")
		info += "{} STL {} BLK".format(stl2, blk2) + "\n"
		info += "{} FG% {} 3P% {} FT%".format(fg, threePointPer, ft).ljust(CENTER, " ")
		info += "{} FG% {} 3P% {} FT%".format(fg2, threePointPer2, ft2) + "\n"
		info += "{} 3PM  {} Games Played  {} Games Started".format(threepm, gp, gs).ljust(CENTER, " ")
		info += "{} 3PM  {} Games Played  {} Games Started".format(threepm2, gp2, gs2) + "\n"

		info += "_"*87 + "\n" + "COMPARISON" + "\n"

		# Calculating average fantasy points scored per game
		fga = player1.fga
		fgm = player1.fg
		fta = player1.fta
		ftm = player1.ftm

		fga2 = player2.fga
		fgm2 = player2.fg
		fta2 = player2.fta
		ftm2 = player2.ftm

		# w is for weight
		wfga=float(response.POST.get("fga"))
		wfgm=float(response.POST.get("fgm"))
		wfta=float(response.POST.get("fta"))
		wftm=float(response.POST.get("ftm"))
		wthreepm=float(response.POST.get("threepm"))
		wpts=float(response.POST.get("pts"))
		wreb=float(response.POST.get("reb"))
		wast=float(response.POST.get("ast"))
		wstl=float(response.POST.get("stl"))
		wblk=float(response.POST.get("blk"))
		wtov=float(response.POST.get("tov"))

		fPointTot = wfga*float(fga) + wfgm*float(fgm) + wfta*float(fta) + wftm*float(ftm) + \
					wthreepm*float(threepm) + wpts*float(pts) + wreb*float(reb) + wast*float(ast) + \
					wstl*float(stl) + wblk*float(blk) + wtov*float(turnover)

		fPointTot = round(fPointTot, 2)

		fPointTot2 = wfga*float(fga2) + wfgm*float(fgm2) + wfta*float(fta2) + wftm*float(ftm2) + \
					wthreepm*float(threepm2) + wpts*float(pts2) + wreb*float(reb2) + wast*float(ast2) + \
					wstl*float(stl2) + wblk*float(blk2) + wtov*float(turnover2)
		fPointTot2 = round(fPointTot2, 2)

		info += "{} averaged {} fantasy points per game\n".format(name, fPointTot)
		info += "{} averaged {} fantasy points per game\n".format(name2, fPointTot2)

		if fPointTot > fPointTot2:
			info += "Therefore, {} averaged {} more fantasy points than {}".format(name, \
						round(fPointTot-fPointTot2,2), name2)
		elif fPointTot < fPointTot2:
			info += "Therefore, {} averaged {} more fantasy points than {}".format(name2, \
						round(fPointTot2-fPointTot,2), name)
		else:
			info += "Therefore, {} and {} averaged the same amount of fantasy points".format(name, name2)

		



		return render(response, "main/points.html", {"pointsForm": pointsForm, "playerForm":playerForm, "info":info})

	playerForm = PlayerForm()
	pointsForm = PointsForm(initial={'fga': -0.45, 'fgm': 1.0, 'fta': -0.75, 'ftm': 1.0, 'threepm': 3.0, 
								'pts': 0.5, 'reb': 1.5, 'ast': 2.0, 'stl': 3.0, 'blk': 3.0, 'tov': -2.0,})
	info = ""
	return render(response, "main/points.html", {"pointsForm": pointsForm, "playerForm":playerForm, "info":info})