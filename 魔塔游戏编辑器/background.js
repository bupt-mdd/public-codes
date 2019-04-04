
var LOGIC_W=13;
var UNIT_LENGTH=canvas.width/LOGIC_W;
var img1= new Image();
img1.src="face.jpg";
var img2= new Image();
img2.src="monsterlib1.png";
var img3= new Image();
img3.src="Floor.png";

var defineProperty=[  //h for health point,a for attack,d for defense,g for gold,e for experience
    {h:850,a:350,d:200,g:45,e:35,id:9},//golden guard黄金卫兵
    {h:35,a:18,d:1,g:1,e:1,id:10},//green slime绿头怪
    {h:50,a:20,d:2,g:2,e:1,id:11},//black slime黑头怪
    {h:70,a:25,d:100,g:35,e:20,id:12},//black slime with swore黑头怪
    {h:220,a:120,d:70,g:20,e:15,id:13},//Linen master麻衣法师
    {h:80,a:28,d:3,g:3,e:2,id:14},//white eye slime白眼怪
    {h:15000,a:1000,d:1000,g:100,e:100,id:15},//red devil红衣魔王
    {h:45000,a:2550,d:2250,g:312,e:275,id:16},//devil冥灵魔王2
    {h:1200,a:620,d:520,g:65,e:50,id:17},//Doppelsoldner双手剑士
    {h:1500,a:650,d:550,g:70,e:55,id:18},//Doppelsoldner双手剑士2
    {h:55,a:23,d:3,g:3,e:3,id:19},//blue slime蓝头怪
    {h:80,a:30,d:5,g:5,e:5,id:20},//colorful slime彩色头怪
    {h:30000,a:1700,d:1500,g:250,e:220,id:21},//related devil冥灵魔王
     {h:170,a:95,d:0,g:17,e:17,id:22},//girl女孩
    {h:40,a:20,d:3,g:1,e:1,id:23},//girl女孩
    {h:110,a:25,d:5,g:5,e:6,id:24},//red skeleton红骷髅
    {h:120,a:26,d:6,g:6,e:7,id:25},//brown skeleton红骷髅
    {h:125,a:27,d:7,g:7,e:8,id:26},//yellow skeleton黄骷髅
    {h:130,a:28,d:8,g:8,e:9,id:27},//white skeleton白骷髅
    {h:100,a:20,d:5,g:3,e:2,id:28},//white bat白蝙蝠
    {h:105,a:21,d:5,g:4,e:3,id:29},//red bat红蝙蝠
    {h:150,a:65,d:30,g:10,e:8,id:30},//big bat大蝙蝠
    {h:110,a:22,d:6,g:4,e:3,id:31},//yellow bat黄蝙蝠
    {h:115,a:23,d:6,g:5,e:4,id:32},//grey bat灰蝙蝠
    {h:160,a:70,d:35,g:13,e:10,id:33},//black big bat黑色大蝙蝠
    {h:1300,a:630,d:525,g:68,e:53,id:34},//Doppelsoldner双手剑士3
    {h:1350,a:640,d:530,g:69,e:54,id:35},//Doppelsoldner双手剑士4
    {h:1400,a:645,d:560,g:70,e:55,id:36},//Doppelsoldner with shield带盾牌的双手剑士
    {h:1355,a:643,d:535,g:69,e:54,id:37},//Doppelsoldner双手剑士
    {h:450,a:150,d:90,g:22,e:19,id:38},//junior guard初级卫兵
    {h:500,a:200,d:150,g:45,e:45,id:39},//medium guard中级卫兵
    {h:1500,a:560,d:460,g:60,e:50,id:40},//senior guard高级卫兵
    {h:460,a:160,d:95,g:28,e:25,id:41},//white gurad初级卫兵2
    {h:500,a:170,d:160,g:45,e:45,id:42},//guard with shield带盾牌的卫兵
    {h:1600,a:580,d:480,g:65,e:60,id:43},//senior guard高级卫兵2
    {h:50,a:100,d:50,g:15,e:13,id:44},//junior mage初级法师
    {h:80,a:150,d:80,g:25,e:20,id:45},//Intermediate master中级法师
    {h:100,a:200,d:110,g:30,e:25,id:46},//senior mage高级法师
    {h:110,a:230,d:130,g:35,e:30,id:47},//black senior mage黑色高级法师
    {h:210,a:200,d:65,g:45,e:45,id:48},//warrior战士
    {h:160,a:230,d:100,g:65,e:65,id:49},//knight骑士
    {h:250,a:55,d:35,g:0,e:0,id:50},//senior warrior高级战士
    {h:320,a:140,d:20,g:30,e:30,id:51},//ghost幽灵
    {h:330,a:150,d:25,g:35,e:35,id:52},//white ghost白色幽灵
    {h:350,a:200,d:30,g:40,e:40,id:53},//senior ghost高级幽灵
    {h:100,a:0,d:0,g:0,e:0,id:81},//potion红药水，提升微量生命值
    {h:300,a:0,d:0,g:0,e:0,id:82},//蓝药水，提升小量生命值
    {h:500,a:0,d:0,g:0,e:0,id:83},//绿药水，提升中量生命值
    {h:1000,a:0,d:0,g:0,e:0,id:84},//蓝药水，提升大量生命值
    //{h:100,a:0,d:0,g:0,e:0,id:85},//magic bottle解除相应的状态，解衰
    //{h:100,a:0,d:0,g:0,e:0,id:86},//解毒
    //{h:100,a:0,d:0,g:0,e:0,id:87},//解慢
    //{h:100,a:0,d:0,g:0,e:0,id:88},//解咒
    {h:50,a:0,d:0,g:0,e:0,id:89},//junior potion提升小量生命值+50*区域数
    {h:100,a:0,d:0,g:0,e:0,id:90},//medium potion提升中量生命值+55*区域数
    {h:200,a:0,d:0,g:0,e:0,id:91},//senior potion提升大量生命值+60*区域数
    // {x:96,y:256,w:32,h:32,id:92},
    {h:60,a:0,d:0,g:0,e:0,id:93},//junior potion提升小量生命值+200*区域数
    {h:120,a:0,d:0,g:0,e:0,id:94},//medium potion提升中量生命值+250+区域数
    {h:240,a:0,d:0,g:0,e:0,id:95},//senior potion提升大量生命值+300*区域数
    //{x:224,y:256,w:32,h:32,id:96},
    {h:0,a:50,d:0,g:0,e:0,id:97},//gem红宝石 提升勇士小量攻击
    {h:0,a:0,d:50,g:0,e:0,id:98},//蓝宝石 提升勇士小量防御
    //{h:0,a:0,d:0,g:0,e:0,id:99},//绿宝石 提升勇士小量魔防
    //{h:0,a:0,d:0,g:0,e:0,id:100},//黄宝石 提升勇士小量等级并加点提升能力值
    {h:0,a:100,d:0,g:0,e:0,id:101},//红宝石 提升勇士中量攻击
    {h:0,a:0,d:100,g:0,e:0,id:102},//蓝宝石 提升勇士中量防御
    //{h:0,a:0,d:0,g:0,e:0,id:103},//绿宝石 提升勇士中量魔防
    //{h:0,a:0,d:0,g:0,e:0,id:104},//黄宝石 提升勇士重量等级并提升能力值
    {h:0,a:300,d:0,g:0,e:0,id:105},//红月亮 提升勇士大量攻击
    {h:0,a:0,d:300,g:0,e:0,id:106},//蓝月亮 提升勇士大量防御
    //{h:100,a:0,d:0,g:0,e:0,id:107},//绿月亮 提升勇士大量魔防
    //{h:100,a:0,d:0,g:0,e:0,id:108},//黄月亮 提升勇士大量等级并提升能力值
    {h:0,a:500,d:0,g:0,e:0,id:109},//红宝石 提升勇士超大量攻击
    {h:0,a:0,d:500,g:0,e:0,id:110},//蓝宝石 提升勇士超大量防御
    //{h:0,a:0,d:0,g:0,e:0,id:111},//绿宝石 提升勇士超大量魔防
    //{h:0,a:0,d:0,g:0,e:0,id:112},//黄宝石 提升勇士超大量等级并加点能力值
    {h:0,a:10,d:0,g:0,e:0,id:113},//swore剑攻击+10
    {h:0,a:20,d:0,g:0,e:0,id:114},//攻击+20
    {h:0,a:50,d:0,g:0,e:0,id:115},//攻击+50
    {h:0,a:60,d:0,g:0,e:0,id:116},//攻击+60
    {h:0,a:100,d:0,g:0,e:0,id:117},//攻击+100
    {h:0,a:110,d:0,g:0,e:0,id:118},//攻击+110
    {h:0,a:70,d:0,g:0,e:0,id:119},//攻击+70
    {h:0,a:80,d:0,g:0,e:0,id:120}//攻击+80
];

var inputcells=[
    {x:0,y:0,w:32,h:32,id:0},//white door
    {x:32,y:0,w:32,h:32,id:0},
    {x:64,y:0,w:32,h:32,id:0},
    {x:96,y:0,w:32,h:32,id:0},
    {x:128,y:0,w:32,h:32,id:1},//yellow door
    {x:160,y:0,w:32,h:32,id:1},
    {x:192,y:0,w:32,h:32,id:1},
    {x:224,y:0,w:32,h:32,id:1},
    {x:256,y:0,w:32,h:32,id:2},//red background
    {x:288,y:0,w:32,h:32,id:2},
    {x:320,y:0,w:32,h:32,id:2},
    {x:352,y:0,w:32,h:32,id:2},
    {x:384,y:0,w:32,h:32,id:3},//blue background
    {x:416,y:0,w:32,h:32,id:3},
    {x:448,y:0,w:32,h:32,id:3},
    {x:480,y:0,w:32,h:32,id:3},
    {x:512,y:0,w:32,h:32,id:4},//black background
    {x:544,y:0,w:32,h:32,id:4},
    {x:576,y:0,w:32,h:32,id:4},
    {x:608,y:0,w:32,h:32,id:4},
    {x:640,y:0,w:32,h:32,id:5},//upstairs
    {x:672,y:0,w:32,h:32,id:5},
    {x:704,y:0,w:32,h:32,id:5},
    {x:736,y:0,w:32,h:32,id:5},
    {x:768,y:0,w:32,h:32,id:6},//downstairs
    {x:800,y:0,w:32,h:32,id:6},
    {x:832,y:0,w:32,h:32,id:6},
    {x:864,y:0,w:32,h:32,id:6},
    {x:896,y:0,w:32,h:32,id:7},//brown door
    {x:928,y:0,w:32,h:32,id:7},
    {x:960,y:0,w:32,h:32,id:7},
    {x:992,y:0,w:32,h:32,id:7},
    {x:0,y:32,w:32,h:32,id:8},//fairy
    {x:32,y:32,w:32,h:32,id:8},
    {x:64,y:32,w:32,h:32,id:8},
    {x:96,y:32,w:32,h:32,id:8},
    {x:128,y:32,w:32,h:32,id:9},//golden guard
    {x:160,y:32,w:32,h:32,id:9},
    {x:192,y:32,w:32,h:32,id:9},
    {x:224,y:32,w:32,h:32,id:9},
    {x:256,y:32,w:32,h:32,id:10},//red slime
    {x:288,y:32,w:32,h:32,id:10},
    {x:320,y:32,w:32,h:32,id:10},
    {x:352,y:32,w:32,h:32,id:10},
    {x:384,y:32,w:32,h:32,id:11},//black slime
    {x:416,y:32,w:32,h:32,id:11},
    {x:448,y:32,w:32,h:32,id:11},
    {x:480,y:32,w:32,h:32,id:11},
    {x:512,y:32,w:32,h:32,id:12},//black slime with swore and shield
    {x:544,y:32,w:32,h:32,id:12},
    {x:576,y:32,w:32,h:32,id:12},
    {x:608,y:32,w:32,h:32,id:12},
    {x:640,y:32,w:32,h:32,id:13},//Linen master
    {x:672,y:32,w:32,h:32,id:13},
    {x:704,y:32,w:32,h:32,id:13},
    {x:736,y:32,w:32,h:32,id:13},
    {x:768,y:32,w:32,h:32,id:14},//eye slime
    {x:800,y:32,w:32,h:32,id:14},
    {x:832,y:32,w:32,h:32,id:14},
    {x:864,y:32,w:32,h:32,id:14},
    {x:896,y:32,w:32,h:32,id:15},//red devil
    {x:928,y:32,w:32,h:32,id:15},
    {x:960,y:32,w:32,h:32,id:15},
    {x:992,y:32,w:32,h:32,id:15},
    {x:0,y:64,w:32,h:32,id:16},// devil
    {x:32,y:64,w:32,h:32,id:16},
    {x:64,y:64,w:32,h:32,id:16},
    {x:96,y:64,w:32,h:32,id:16},
    {x:128,y:64,w:32,h:32,id:17},//Doppelsoldner
    {x:160,y:64,w:32,h:32,id:17},
    {x:192,y:64,w:32,h:32,id:17},
    {x:224,y:64,w:32,h:32,id:17},
    {x:256,y:64,w:32,h:32,id:18},//Doppelsoldner
    {x:288,y:64,w:32,h:32,id:18},
    {x:320,y:64,w:32,h:32,id:18},
    {x:352,y:64,w:32,h:32,id:18},
    {x:384,y:64,w:32,h:32,id:19},//blue slime
    {x:416,y:64,w:32,h:32,id:19},
    {x:448,y:64,w:32,h:32,id:19},
    {x:480,y:64,w:32,h:32,id:19},
    {x:512,y:64,w:32,h:32,id:20},//colorful slime
    {x:544,y:64,w:32,h:32,id:20},
    {x:576,y:64,w:32,h:32,id:20},
    {x:608,y:64,w:32,h:32,id:20},
    {x:640,y:64,w:32,h:32,id:21},//related devil
    {x:672,y:64,w:32,h:32,id:21},
    {x:704,y:64,w:32,h:32,id:21},
    {x:736,y:64,w:32,h:32,id:21},
    {x:768,y:64,w:32,h:32,id:22},//girl
    {x:800,y:64,w:32,h:32,id:22},
    {x:832,y:64,w:32,h:32,id:22},
    {x:864,y:64,w:32,h:32,id:22},
    {x:896,y:64,w:32,h:32,id:23},//girl
    {x:928,y:64,w:32,h:32,id:23},
    {x:960,y:64,w:32,h:32,id:23},
    {x:992,y:64,w:32,h:32,id:23},
    {x:0,y:96,w:32,h:32,id:24},//red skeleton
    {x:32,y:96,w:32,h:32,id:24},
    {x:64,y:96,w:32,h:32,id:24},
    {x:96,y:96,w:32,h:32,id:24},
    {x:128,y:96,w:32,h:32,id:25},//brown skeleton
    {x:160,y:96,w:32,h:32,id:25},
    {x:192,y:96,w:32,h:32,id:25},
    {x:224,y:96,w:32,h:32,id:25},
    {x:256,y:96,w:32,h:32,id:26},//yellow skeleton
    {x:288,y:96,w:32,h:32,id:26},
    {x:320,y:96,w:32,h:32,id:26},
    {x:352,y:96,w:32,h:32,id:26},
    {x:384,y:96,w:32,h:32,id:27},//white skeleton
    {x:416,y:96,w:32,h:32,id:27},
    {x:448,y:96,w:32,h:32,id:27},
    {x:480,y:96,w:32,h:32,id:27},
    {x:512,y:96,w:32,h:32,id:28},//bat
    {x:544,y:96,w:32,h:32,id:28},
    {x:576,y:96,w:32,h:32,id:28},
    {x:608,y:96,w:32,h:32,id:28},
    {x:640,y:96,w:32,h:32,id:29},//red bat
    {x:672,y:96,w:32,h:32,id:29},
    {x:704,y:96,w:32,h:32,id:29},
    {x:736,y:96,w:32,h:32,id:29},
    {x:768,y:96,w:32,h:32,id:30},//big bat
    {x:800,y:96,w:32,h:32,id:30},
    {x:832,y:96,w:32,h:32,id:30},
    {x:864,y:96,w:32,h:32,id:30},
    {x:896,y:96,w:32,h:32,id:31},//yellow bat
    {x:928,y:96,w:32,h:32,id:31},
    {x:960,y:96,w:32,h:32,id:31},
    {x:992,y:96,w:32,h:32,id:31},
    {x:0,y:128,w:32,h:32,id:32},//grey bat
    {x:32,y:128,w:32,h:32,id:32},
    {x:64,y:128,w:32,h:32,id:32},
    {x:96,y:128,w:32,h:32,id:32},
    {x:128,y:128,w:32,h:32,id:33},//black bat
    {x:160,y:128,w:32,h:32,id:33},
    {x:192,y:128,w:32,h:32,id:33},
    {x:224,y:128,w:32,h:32,id:33},
    {x:256,y:128,w:32,h:32,id:34},//brown Doppelsoldner
    {x:288,y:128,w:32,h:32,id:34},
    {x:320,y:128,w:32,h:32,id:34},
    {x:352,y:128,w:32,h:32,id:34},
    {x:384,y:128,w:32,h:32,id:35},//yellow Doppelsoldner
    {x:416,y:128,w:32,h:32,id:35},
    {x:448,y:128,w:32,h:32,id:35},
    {x:480,y:128,w:32,h:32,id:35},
    {x:512,y:128,w:32,h:32,id:36},//Doppelsoldner with shield
    {x:544,y:128,w:32,h:32,id:36},
    {x:576,y:128,w:32,h:32,id:36},
    {x:608,y:128,w:32,h:32,id:36},
    {x:640,y:128,w:32,h:32,id:37},//purple Doppelsoldner
    {x:672,y:128,w:32,h:32,id:37},
    {x:704,y:128,w:32,h:32,id:37},
    {x:736,y:128,w:32,h:32,id:37},
    {x:768,y:128,w:32,h:32,id:38},//Junior guard
    {x:800,y:128,w:32,h:32,id:38},
    {x:832,y:128,w:32,h:32,id:38},
    {x:864,y:128,w:32,h:32,id:38},
    {x:896,y:128,w:32,h:32,id:39},//Intermediate guard
    {x:928,y:128,w:32,h:32,id:39},
    {x:960,y:128,w:32,h:32,id:39},
    {x:992,y:128,w:32,h:32,id:39},
    {x:0,y:160,w:32,h:32,id:40},//senior guard
    {x:32,y:160,w:32,h:32,id:40},
    {x:64,y:160,w:32,h:32,id:40},
    {x:96,y:160,w:32,h:32,id:40},
    {x:128,y:160,w:32,h:32,id:41},//white guard
    {x:160,y:160,w:32,h:32,id:41},
    {x:192,y:160,w:32,h:32,id:41},
    {x:224,y:160,w:32,h:32,id:41},
    {x:256,y:160,w:32,h:32,id:42},//guard with shiled
    {x:288,y:160,w:32,h:32,id:42},
    {x:320,y:160,w:32,h:32,id:42},
    {x:352,y:160,w:32,h:32,id:42},
    {x:384,y:160,w:32,h:32,id:43},//senior guard
    {x:416,y:160,w:32,h:32,id:43},
    {x:448,y:160,w:32,h:32,id:43},
    {x:480,y:160,w:32,h:32,id:43},
    {x:512,y:160,w:32,h:32,id:44},//Junior mage
    {x:544,y:160,w:32,h:32,id:44},
    {x:576,y:160,w:32,h:32,id:44},
    {x:608,y:160,w:32,h:32,id:44},
    {x:640,y:160,w:32,h:32,id:45},//Intermediate master
    {x:672,y:160,w:32,h:32,id:45},
    {x:704,y:160,w:32,h:32,id:45},
    {x:736,y:160,w:32,h:32,id:45},
    {x:768,y:160,w:32,h:32,id:46},//senior mage
    {x:800,y:160,w:32,h:32,id:46},
    {x:832,y:160,w:32,h:32,id:46},
    {x:864,y:160,w:32,h:32,id:46},
    {x:896,y:160,w:32,h:32,id:47},//black senior mage
    {x:928,y:160,w:32,h:32,id:47},
    {x:960,y:160,w:32,h:32,id:47},
    {x:992,y:160,w:32,h:32,id:47},
    {x:0,y:192,w:32,h:32,id:48},//ming warrior
    {x:32,y:192,w:32,h:32,id:48},
    {x:64,y:192,w:32,h:32,id:48},
    {x:96,y:192,w:32,h:32,id:48},
    {x:128,y:192,w:32,h:32,id:49},//knight
    {x:160,y:192,w:32,h:32,id:49},
    {x:192,y:192,w:32,h:32,id:49},
    {x:224,y:192,w:32,h:32,id:49},
    {x:256,y:192,w:32,h:32,id:50},//ming senior warrior
    {x:288,y:192,w:32,h:32,id:50},
    {x:320,y:192,w:32,h:32,id:50},
    {x:352,y:192,w:32,h:32,id:50},
    {x:384,y:192,w:32,h:32,id:51},//ghost
    {x:416,y:192,w:32,h:32,id:51},
    {x:448,y:192,w:32,h:32,id:51},
    {x:480,y:192,w:32,h:32,id:51},
    {x:512,y:192,w:32,h:32,id:52},//white ghost
    {x:544,y:192,w:32,h:32,id:52},
    {x:576,y:192,w:32,h:32,id:52},
    {x:608,y:192,w:32,h:32,id:52},
    {x:640,y:192,w:32,h:32,id:53},//black ghost
    {x:672,y:192,w:32,h:32,id:53},
    {x:704,y:192,w:32,h:32,id:53},
    {x:736,y:192,w:32,h:32,id:53},
    {x:768,y:192,w:32,h:32,id:54},//the old man
    {x:800,y:192,w:32,h:32,id:54},
    {x:832,y:192,w:32,h:32,id:54},
    {x:864,y:192,w:32,h:32,id:54},
    {x:896,y:192,w:32,h:32,id:55},//number
    {x:928,y:192,w:32,h:32,id:55},
    {x:960,y:192,w:32,h:32,id:55},
    {x:992,y:192,w:32,h:32,id:55},
    {x:0,y:224,w:32,h:32,id:57},//door
    {x:32,y:224,w:32,h:32,id:58},
    {x:64,y:224,w:32,h:32,id:59},
    {x:96,y:224,w:32,h:32,id:60},
    {x:128,y:224,w:32,h:32,id:61},
    {x:160,y:224,w:32,h:32,id:62},
    {x:192,y:224,w:32,h:32,id:63},
    {x:224,y:224,w:32,h:32,id:64},
    {x:256,y:224,w:32,h:32,id:65},
    {x:288,y:224,w:32,h:32,id:66},
    {x:320,y:224,w:32,h:32,id:67},
    {x:352,y:224,w:32,h:32,id:68},
    {x:384,y:224,w:32,h:32,id:69},
    {x:416,y:224,w:32,h:32,id:70},
    {x:448,y:224,w:32,h:32,id:71},
    {x:480,y:224,w:32,h:32,id:72},
    {x:512,y:224,w:32,h:32,id:73},
    {x:544,y:224,w:32,h:32,id:74},
    {x:576,y:224,w:32,h:32,id:75},
    {x:608,y:224,w:32,h:32,id:76},
    {x:640,y:224,w:32,h:32,id:77},//key
    {x:672,y:224,w:32,h:32,id:78},
    {x:704,y:224,w:32,h:32,id:79},
    {x:736,y:224,w:32,h:32,id:80},
    {x:768,y:224,w:32,h:32,id:81},//potion红药水，提升微量生命值
    {x:800,y:224,w:32,h:32,id:82},//蓝药水，提升小量生命值
    {x:832,y:224,w:32,h:32,id:83},//绿药水，提升中量生命值
    {x:864,y:224,w:32,h:32,id:84},//蓝药水，提升大量生命值
    {x:896,y:224,w:32,h:32,id:85},//magic bottle解除相应的状态，解衰
    {x:928,y:224,w:32,h:32,id:86},//解毒
    {x:960,y:224,w:32,h:32,id:87},//解慢
    {x:992,y:224,w:32,h:32,id:88},//解咒
    {x:0,y:256,w:32,h:32,id:89},//junior potion提升小量生命值+50*区域数
    {x:32,y:256,w:32,h:32,id:90},//medium potion提升中量生命值+55*区域数
    {x:64,y:256,w:32,h:32,id:91},//senior potion提升大量生命值+60*区域数
//{x:96,y:256,w:32,h:32,id:92},
    {x:128,y:256,w:32,h:32,id:93},//junior potion提升小量生命值+200*区域数
    {x:160,y:256,w:32,h:32,id:94},//medium potion提升中量生命值+250+区域数
    {x:192,y:256,w:32,h:32,id:95},//senior potion提升大量生命值+300*区域数
//{x:224,y:256,w:32,h:32,id:96},
    {x:256,y:256,w:32,h:32,id:97},//gem红宝石 提升勇士小量攻击
    {x:288,y:256,w:32,h:32,id:98},//蓝宝石 提升勇士小量防御
    {x:320,y:256,w:32,h:32,id:99},//绿宝石 提升勇士小量魔防
    {x:352,y:256,w:32,h:32,id:100},//黄宝石 提升勇士小量等级并加点提升能力值
    {x:384,y:256,w:32,h:32,id:101},//红宝石 提升勇士中量攻击
    {x:416,y:256,w:32,h:32,id:102},//蓝宝石 提升勇士中量防御
    {x:448,y:256,w:32,h:32,id:103},//绿宝石 提升勇士中量魔防
    {x:480,y:256,w:32,h:32,id:104},//黄宝石 提升勇士重量等级并提升能力值
    {x:512,y:256,w:32,h:32,id:105},//红月亮 提升勇士大量攻击
    {x:544,y:256,w:32,h:32,id:106},//蓝月亮 提升勇士大量防御
    {x:576,y:256,w:32,h:32,id:107},//绿月亮 提升勇士大量魔防
    {x:608,y:256,w:32,h:32,id:108},//黄月亮 提升勇士大量等级并提升能力值
    {x:640,y:256,w:32,h:32,id:109},//红宝石 提升勇士超大量攻击
    {x:672,y:256,w:32,h:32,id:110},//蓝宝石 提升勇士超大量防御
    {x:704,y:256,w:32,h:32,id:111},//绿宝石 提升勇士超大量魔防
    {x:736,y:256,w:32,h:32,id:112},//黄宝石 提升勇士超大量等级并加点能力值
    {x:768,y:256,w:32,h:32,id:113},//swore剑攻击+10
    {x:800,y:256,w:32,h:32,id:114},//攻击+20
    {x:832,y:256,w:32,h:32,id:115},//攻击+50
    {x:864,y:256,w:32,h:32,id:116},//攻击+60
    {x:896,y:256,w:32,h:32,id:117},//攻击+100
    {x:928,y:256,w:32,h:32,id:118},//攻击+110
    {x:960,y:256,w:32,h:32,id:119},//攻击+70
    {x:992,y:256,w:32,h:32,id:120},//攻击+80
]



var Sprite=function(name,painter,behavors,appender){
    if(name!==undefined)
        this.name=name;
    if(painter!==undefined)
        this.painter=painter;
    if(appender!==undefined)
        this.appender=appender;
    this.x=0;
    this.y=0;
    this.vec_x=1;
    this.height=1;
    this.width=1;//，应该无影响
    this.animating=false;
    this.visible=true;
    this.behavors=behavors||[];
    this.collision=undefined;
};
Sprite.prototype={
    paint:function(context) {
       // alert("paint");
        if (this.painter !== undefined && this.visible)
            this.painter.paint(this,context);
    },
    update: function(context,time){
        for(i=0;i<this.behavors.length;i++){
            this.behavors[i].excute(this,context,time);}
    }
};
var imgpainter=function(url){
    this.img=new Image();
    this.img.src=url;
};
function trans(e){
    return +(e*UNIT_LENGTH);
}
imgpainter.prototype={
    paint:function(sprite,context){
        if(this.img.complete){
            context.drawImage(this.img,trans(sprite.x),trans(sprite.y),trans(sprite.width),trans(sprite.height));
            return true;
        }
        return false;
    }
};

var  spriteSheetPainter=function(img1,cells){
    this.img=img1;
    this.cells=cells||[];
    this.index=0;
}
spriteSheetPainter.prototype={
    advance: function(){
        if(this.index===this.cells.length-1)
            this.index=0;
        else this.index++;
    },
    paint:function(sprite,context){
        var cell=this.cells[this.index];
        if(this.img.complete){
            context.drawImage(this.img,cell.x,cell.y,cell.w,cell.h,trans(sprite.x),trans(sprite.y),trans(sprite.width),trans(sprite.height));
            return true;
        }
        return false;
    }
};

var stopwatch=function(){
    this.startTime=0;
    this.running=false;
    this.elapsed=undefined;
}
stopwatch.prototype={
    start :function(){
        this.startTime=+ new Date();
        this.running=true;
    },
    stop:function(){
        this.running=false;
        this.elapsed=(+new Date())-this.startTime;
    },
    getElapsed:function(){
        if(this.running)
            return (+new Date())-this.startTime;
        else return this.elapsed;
    },
    isRunning: function(){
        return this.running;
    },
    reset: function () {
        this.elapsed=0;
    }
}
var animationTimer=function(t){
    this.duration=t;
}
animationTimer.prototype={
    stopwatch: new stopwatch(),
    start:function(){
        this.stopwatch.start();
    },
    stop: function(){
        this.stopwatch.stop();
    },
    getElapsedTime:function(){
        if(this.stopwatch.running)
            return this.stopwatch.getElapsed();
        else return undefined;
    },
    isOver: function () {
        return this.stopwatch.getElapsed()>this.duration;
    },
    isRunning: function () {
        return this.stopwatch.isRunning();;
    }
}
var changeface=function(TIME_INTERVAL){
    this.last=0;
    this.TIME_INTERVAL=TIME_INTERVAL;
}
changeface.prototype={
    excute: function(sprite,context,time){
        if(time-this.last>this.TIME_INTERVAL)
        {   this.last=time;
            sprite.painter.advance();
        }
    }
}
function createRequest() {
    try {
        request = new XMLHttpRequest();
    } catch (tryMS) {
        try {
            request = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (otherMS) {
            try {
                request = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (failed) {
                request = null;
            }
        }
    }
    return request;
}
var facecells=[
    {x:0,y:0,w:200,h:200},
    {x:233,y:0,w:200,h:200}
];
var monsterInf= function (l,h,a,d,m,e ) {
    this.level=l;
    this.health=h;
    this.attack=a;
    this.defence=d;
    this.money=m;
    this.experience=e;
    this.yk=0;
    this.bk=0;
    this.rk=0;
}

function getMonsterInf(x) {
    for(var i=0;i<defineProperty.length;i++){
        if(defineProperty[i].id==x)
            return defineProperty[i];
    }
    return undefined;
}

