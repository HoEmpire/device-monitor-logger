import sys
from data_type import KeyWord, LogInfo, Date, Span

block_num = 4

keyword_list = [
    "Loading images and feature detection...",
    "Image loading + feature detection time:", "Feature matching...",
    "Matching time:", "Start SFM...", "SFM takes:",
    "Start images correction...", "Finish images correction..."
]

keyword_list += [
    "Start densify...", "Fuse depth map...", "Finish densify...",
    "Filter point cloud", "Creating mesh for"
] * block_num
keyword_list += ["Saving b3dms json tree...", "Collect lod mesh into one end."]

kw = KeyWord(keyword_list)
file_path = sys.argv[1]

file = open(file_path, 'r')
report_file = open("report.txt", 'w')

line = file.readline()
loginfo = []

while (len(line) != 0 and kw.finish_search is not True):
    if (line[0] != '['):
        line = file.readline()
        continue
    time_start_index = line.find('[') + 1
    time_end_index = line.find(']')
    info_start_index = line.find(']', time_end_index + 1) + 1

    if (line.find(kw.keyword_list[kw.cursor], time_end_index + 1) != -1):
        loginfo.append(
            LogInfo(line[time_start_index:time_end_index],
                    Date(line[time_start_index:time_end_index]),
                    line[info_start_index:-1]))
        kw.update_cursor()

    line = file.readline()

file.close()

for l in loginfo:
    l.print()

print("\n")
span = Span("Load image and feature detection", loginfo[0], loginfo[1])
report_file.write(span.report() + "\n")
span = Span("Feature matching", loginfo[2], loginfo[3])
report_file.write(span.report() + "\n")
span = Span("SfM", loginfo[4], loginfo[5])
report_file.write(span.report() + "\n")
span = Span("Sparse reconstruction(all)", loginfo[0], loginfo[5])
span.report()
# report_file.write(span.report() + "\n")

print("\n")

span = Span("Image correction", loginfo[6], loginfo[7])
report_file.write(span.report() + "\n")
for i in range(block_num):
    span = Span("Dense Reconstruction", loginfo[8+5*i], loginfo[9+5*i])
    report_file.write(span.report() + "\n")
    span = Span("Depth map fusion", loginfo[9+5*i], loginfo[10+5*i])
    report_file.write(span.report() + "\n")
    span = Span("Point cloud filtering and saving", loginfo[11+5*i], loginfo[12+5*i])
    report_file.write(span.report() + "\n")
    span = Span("Meshing", loginfo[12+5*i], loginfo[13+5*i])
    report_file.write(span.report() + "\n")
span = Span("Saving Data", loginfo[13+5*(block_num-1)], loginfo[14+5*(block_num-1)])
span.report()
# report_file.write(span.report() + "\n")
span = Span("Dense reconstruction(all)", loginfo[6], loginfo[14+5*(block_num-1)])
span.report()
# report_file.write(span.report() + "\n")

report_file.close()
