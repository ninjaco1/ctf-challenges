#!/usr/bin/env python3

from Crypto.Util.number import *
import secrets
import numpy as np


p = 130434182441603098085956776986813693398366763586020595512987159262899881890442688054651285679445774176839742529438968247167884605733178945825821059309729815062559567359570195682209847084470163302154894657907891113360770217802272940478214121960691147987814527126966323988405399896137541783289094003238223701919

q = 138597380327352419687534641412929290366492126278628014509152301908796041605702001247395731165417386922727859751004918809393586670242582269855310098688232449832555137905517447148665895209928971190929217518775532945000140189878993116900459734922686648711225089388803124904970682571061993115829417981574164016773

N = 18077835991546137626820743332925077231374737772399662733145449713866011668129359761316411770700730249209055598603865901584346720655918002520497560096702556660488788089523716553127902860314936315334492018184193779273443235661432144600266866272632983217297397458819395207649787022607046418182404092209433511795673252554662035312548958373228547867077383341748826769860988734874145040410943724039648358353546951266751272373383570512852677958180656795351767986838842090885711457878146575773989204434421168580537893668075110329840981458434754807779731175606434893879571660655888569704898013958232952940247995442346868287387

c = 15152748367446880771626735564570314364412539866133828878294832734877333779375887301666317343696170583205732549176049143952513352176887862696752491725708864667819416380851470922363167693469581137082049422236381718504826584222025025276217712186948248894030905507578741594465520464407304317496197519614579605451009261929501814390584449735588732230862107938755575264114796923591931144483631719354506203232033044574475941823978540906150537364865247200187073042362762490541339927821746184534026286488138506628489962230620460382693248638990548515405134649935123113868204987749497591513259850481628137175362068619575569454324


euler = (p-1) * (q-1)

d = np.invert(3, euler)

print(long_to_bytes(pow(c,d,N)))
