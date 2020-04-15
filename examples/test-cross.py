from PyCoptimizer.user_parameters import UserParameters
import os
import subprocess
import time
from PyCoptimizer.coptimizer import COptimizer


class Test(UserParameters):
    """ Class to test the abstract class UserParameters 
    """

    def __init__(self):
        super(Test, self).__init__()
        self.dict_optimization = {"no_generations": 30,
                                  "no_pop": 65,
                                  "individual_size": 187,
                                  "crossover_rate": 0.8,
                                  "mutation_rate": 0.005}
        self.min_max = -1
        self.macro = "TUNE"
        self.compile_path = os.getcwd() + "/cross_kalman"
        self.clean_path = os.getcwd() + "/cross_kalman"
        self.flags_list = ["-falign-functions",
                           "-falign-jumps",
                           "-falign-labels",
                           "-falign-loops",
                           "-fauto-inc-dec",  "-fbranch-probabilities",
                           "-fbranch-target-load-optimize", "-fbranch-target-load-optimize2",
                           "-fbtr-bb-exclusive",  "-fcaller-saves",
                           "-fcombine-stack-adjustments",  "-fconserve-stack",
                           "-fcompare-elim",  "-fcprop-registers",  "-fcrossjumping",
                           "-fcse-follow-jumps",  "-fcse-skip-blocks",  "-fcx-fortran-rules",
                           "-fcx-limited-range",
                           "-fdata-sections",  "-fdce",  "-fdelayed-branch",
                           "-fdelete-null-pointer-checks",  "-fdevirtualize",  "-fdevirtualize-speculatively",
                           "-fdevirtualize-at-ltrans",  "-fdse",
                           "-fearly-inlining",  "-fipa-sra",  "-fexpensive-optimizations",  "-ffat-lto-objects",
                           "-ffast-math",  "-ffinite-math-only",  "-ffloat-store",
                           "-fforward-propagate",   "-ffunction-sections",
                           "-fgcse",  "-fgcse-after-reload",  "-fgcse-las",  "-fgcse-lm",  "-fgraphite-identity",
                           "-fgcse-sm",  "-fhoist-adjacent-loads",  "-fif-conversion",
                           "-fif-conversion2",  "-findirect-inlining",
                           "-finline-functions",  "-finline-functions-called-once",
                           "-finline-small-functions",  "-fipa-cp",  "-fipa-cp-clone",
                           "-fipa-pta",  "-fipa-profile",  "-fipa-pure-const",  "-fipa-reference",  "-fipa-icf",
                           "-fira-hoist-pressure",
                           "-fira-loop-pressure",  "-fno-ira-share-save-slots",
                           "-fno-ira-share-spill-slots",
                           "-fisolate-erroneous-paths-dereference",  "-fisolate-erroneous-paths-attribute",
                           "-fivopts",  "-fkeep-inline-functions",
                           "-fkeep-static-consts",  "-flive-range-shrinkage",
                           "-floop-block",  "-floop-interchange",  "-floop-strip-mine",
                           "-floop-unroll-and-jam",  "-floop-nest-optimize",
                           "-floop-parallelize-all",  "-flra-remat",  "-fmerge-all-constants",
                           "-fmerge-constants",  "-fmodulo-sched",  "-fmodulo-sched-allow-regmoves",
                           "-fmove-loop-invariants",  "-fno-branch-count-reg",
                           "-fno-defer-pop",  "-fno-function-cse",
                           "-fno-guess-branch-probability",  "-fno-inline",  "-fno-math-errno",  "-fno-peephole",
                           "-fno-peephole2",  "-fno-sched-interblock",
                           "-fno-sched-spec",  "-fno-signed-zeros",
                           "-fno-toplevel-reorder",  "-fno-trapping-math",  "-fno-zero-initialized-in-bss",
                           "-fomit-frame-pointer",  "-foptimize-sibling-calls",
                           "-fpartial-inlining",  "-fpeel-loops",  "-fpredictive-commoning",
                           "-fprofile-correction",
                           "-fprofile-use", "-fprofile-values",
                           "-fprofile-reorder-functions",
                           "-frename-registers",  "-freorder-blocks",
                           "-freorder-blocks-and-partition",  "-freorder-functions",
                           "-frerun-cse-after-loop",  "-freschedule-modulo-scheduled-loops",
                           "-frounding-math",
                           "-fsched2-use-superblocks",  "-fsched-pressure",
                           "-fsched-spec-load",  "-fsched-spec-load-dangerous",
                           "-fsched-stalled-insns-dep",  "-fsched-stalled-insns",
                           "-fsched-group-heuristic",  "-fsched-critical-path-heuristic",
                           "-fsched-spec-insn-heuristic",  "-fsched-rank-heuristic",
                           "-fsched-last-insn-heuristic",  "-fsched-dep-count-heuristic",
                           "-fschedule-fusion",
                           "-fschedule-insns",
                           "-fselective-scheduling",  "-fselective-scheduling2",
                           "-fsel-sched-pipelining",  "-fsel-sched-pipelining-outer-loops",
                           "-fsemantic-interposition",  "-fshrink-wrap",
                           "-fsignaling-nans",
                           "-fsplit-ivs-in-unroller",
                           "-fsplit-wide-types",  "-fssa-phiopt",
                           "-fstdarg-opt",   "-fstrict-aliasing",
                           "-fthread-jumps",  "-ftracer",  "-ftree-bit-ccp",
                           "-ftree-builtin-call-dce",  "-ftree-ccp",  "-ftree-ch",
                           "-ftree-coalesce-vars",  "-ftree-copy-prop",  "-ftree-dce",  "-ftree-dominator-opts",
                           "-ftree-dse",  "-ftree-forwprop",  "-ftree-fre",
                           "-ftree-loop-if-convert",  "-ftree-loop-im",
                           "-ftree-phiprop",  "-ftree-loop-distribution",  "-ftree-loop-distribute-patterns",
                           "-ftree-loop-ivcanon",  "-ftree-loop-linear",  "-ftree-loop-optimize",
                           "-ftree-loop-vectorize", "-ftree-pre",  "-ftree-partial-pre",  "-ftree-pta",
                           "-ftree-reassoc",   "-ftree-sink",   "-ftree-slsr",   "-ftree-sra",
                           "-ftree-switch-conversion",   "-ftree-tail-merge",
                           "-ftree-ter",   "-ftree-vectorize",   "-ftree-vrp",
                           "-funit-at-a-time",   "-funroll-all-loops",   "-funroll-loops",
                           "-funsafe-math-optimizations",   "-funswitch-loops",
                           "-fipa-ra",   "-fvariable-expansion-in-unroller",   "-fvect-cost-model",   "-fvpt",
                           "-fweb",   "-fuse-linker-plugin",
                           "-O",   "-O0",   "-O1",   "-O2",   "-O3",   "-Os",   "-Ofast",  "-Og"]
        self.static_flags = "-march=native"

    def arguments_to_run_code(self):
        """ Implementing the method arguments_to_run_code.
            This method returns the command to run the executable file
        """
        return "./cross_kalman -n1000"

    def evaluation_function(self):
        """ Implementing the method evaluation_functionn.
            This method returns the value to be optimized by the 
            framework.
            In this method, the user needs to run the executable file 
            and get the value to pass
            to the framework.
        """
        def_path = os.getcwd()
        os.chdir(self.compile_path)

        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]

        my_command = self.arguments_to_run_code()
        # 
        p = subprocess.Popen(my_command, shell=True,
                             stdout=subprocess.PIPE)
        out, err = p.communicate()
        #print("TESTE OUT: ", out)
        #processing the output to get the value        
        output = ''.join(str(out))
        #print output
        output = output.split(' ')
        index = [i for i, s in enumerate(output) if 'throughput' in s]  
        #d = filter(lambda c: 'throughput' in c, output)
        #print("OUTPUT: ", output, list(d))
        #value = output[output.index(d[1]) +4]
        #it tests if has some output
        #if haven't, put value = 0
        if len(output) > 0:
            value = output[index[-1]+1]
            #value = output[output.index(d[1]) +4]
        else:
            value = 0.0
        #print(value, float(value))      
        value = float(value)

        #print("VALOR: ", value)
        os.chdir(def_path)
        return value

    def pre(self):
        pass

    def pos(self):
        pass


if __name__ == '__main__':
    COptimizer().main()
