import nflgame
from phue import Bridge
import time

def handleupdate(active, completed, diffs):
    
    for diff in diffs:
        
        for p in diff.plays:
            
            print p
            
            if (p.team == 'ATL' and (p.touchdown == True or p.kicking_fgm>0)):
                
                b = Bridge(ip='192.168.1.176',username='hV8sjEd6bLs8Bo9M7UJlVM8sYC4UbHWtO54SN62K')
                
                b.set_group(0, {'alert': 'lselect', 'hue': 0, 'sat': 220 })

                time.sleep(5)

                b.set_group(0, {'alert': 'none', 'ct': 443})
    
nflgame.live.run(handleupdate)
