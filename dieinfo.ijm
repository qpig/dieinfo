//open("/Users/zhuxiaoqiang/Desktop/my_sync/dieshot/kunpeng920 cpu.png");
//roiManager("Open", "/Users/zhuxiaoqiang/github/dieinfo/kunpeng920/RoiSet.zip");
roiManager("Show All");
roiManager("Show All with labels");
RoiManager.useNamesAsLabels(true);

run("Set Measurements...", "area display redirect=None decimal=3");
roiManager("Select", newArray(0,1));
roiManager("Measure");