import testExecEngine as TEE
import Utilities as u

if __name__ == '__main__':
    u.printInfo('Initiating Sanity Check...')
    result = TEE.sanityCheck()
    #if(result['status'] ==  True):
       #TEE.functionalTest([])
    #retVal = TEE.functionalTest(['http://intranet.iiit.ac.in/UG1-TimeTable-M13.pdf', 'http://intranet.iiit.ac.in/fee-Spring2008.htm', 'http://intranet.iiit.ac.in/index.css', 'http://intranet.iiit.ac.in/Summer_Projects_2013.pdf', 'http://intranet.iiit.ac.in/UG1-Tutorial-Lab-Schedule-M13.pdf', 'http://intranet.iiit.ac.in/qualifier_Oct09_schedule.html', 'http://intranet.iiit.ac.in/music_club/', 'http://intranet.iiit.ac.in/Information/phd_exam/index.html', 'http://intranet.iiit.ac.in/overload.htm', 'http://intranet.iiit.ac.in/Information/academic/offerings-Spring10.pdf', 'http://intranet.iiit.ac.in/consol_timetable_M2010.pdf', 'http://intranet.iiit.ac.in/Information/academic/almanac-Monsoon2011.pdf', 'http://intranet.iiit.ac.in/library/librarysite/', 'http://intranet.iiit.ac.in/Syllabus-Electives-M2011.pdf', 'http://intranet.iiit.ac.in/CourseOfferings-V6_M2013.pdf'])
    #retVal = TEE.functionalTest(['http://intranet.iiit.ac.in/fee-Spring2008.htm'])
    print result
    #TEE.stressTest()
    
