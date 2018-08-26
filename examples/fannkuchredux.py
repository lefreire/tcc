from PyCoptimizer.user_parameters import UserParameters
import os
import subprocess
import time
from PyCoptimizer.coptimizer import COptimizer


class Fannkuchredux(UserParameters):
    """ Class to test the abstract class UserParameters 
    """

    def __init__(self):
        super(Fannkuchredux, self).__init__()
        self.dict_optimization = {"no_generations": 3,
                                  "no_pop": 2,
                                  "individual_size": 3,
                                  "crossover_rate": 0.3,
                                  "mutation_rate": 0.1}
        self.compile_path = os.getcwd() + "/fannkuch"
        self.clean_path = os.getcwd() + "/fannkuch"
        self.flags_list = ["-faggressive-loop-optimizations", 
                           "-falign-functions",
                           "-falign-jumps",
                            "-falign-labels",
                            "-falign-loops",
                            "-fauto-inc-dec",  "-fbranch-probabilities", 
                            "-fbranch-target-load-optimize",  "-fbranch-target-load-optimize2", 
                            "-fbtr-bb-exclusive",  "-fcaller-saves", 
                            "-fcombine-stack-adjustments",  "-fconserve-stack", 
                            "-fcompare-elim",  "-fcprop-registers",  "-fcrossjumping" ,
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
                            "-floop-parallelize-all",  "-flra-remat",  "-flto", "-fmerge-all-constants", 
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
                            "-fsingle-precision-constant",  "-fsplit-ivs-in-unroller",  
                            "-fsplit-wide-types",  "-fssa-phiopt", 
                            "-fstdarg-opt",   "-fstrict-aliasing", 
                            "-fthread-jumps",  "-ftracer",  "-ftree-bit-ccp", 
                            "-ftree-builtin-call-dce",  "-ftree-ccp",  "-ftree-ch", 
                            "-ftree-coalesce-vars",  "-ftree-copy-prop",  "-ftree-dce",  "-ftree-dominator-opts", 
                            "-ftree-dse",  "-ftree-forwprop",  "-ftree-fre",
                            "-ftree-loop-if-convert",  "-ftree-loop-im", 
                            "-ftree-phiprop",  "-ftree-loop-distribution",  "-ftree-loop-distribute-patterns" ,
                            "-ftree-loop-ivcanon",  "-ftree-loop-linear",  "-ftree-loop-optimize", 
                            "-ftree-loop-vectorize", "-ftree-pre",  "-ftree-partial-pre",  "-ftree-pta", 
                            "-ftree-reassoc",   "-ftree-sink",   "-ftree-slsr",   "-ftree-sra", 
                            "-ftree-switch-conversion",   "-ftree-tail-merge",  
                            "-ftree-ter",   "-ftree-vectorize",   "-ftree-vrp", 
                            "-funit-at-a-time",   "-funroll-all-loops",   "-funroll-loops",  
                            "-funsafe-math-optimizations",   "-funswitch-loops",  
                            "-fipa-ra",   "-fvariable-expansion-in-unroller",   "-fvect-cost-model",   "-fvpt",  
                            "-fweb",   "-fwhole-program",  "-fuse-linker-plugin",  
                            "-O",   "-O0",   "-O1",   "-O2",   "-O3",   "-Os",   "-Ofast",  "-Og"]
        self.static_flags = "-march=native"

    def arguments_to_run_code(self):
        """ Implementing the method arguments_to_run_code.
            This method returns the command to run the executable file
        """
        return "./fannkuchredux.gpp-5.gpp_run 12"

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
        # counting time
        t0 = time.time()
        p = subprocess.Popen(my_command, shell=True,
                             stdout=subprocess.PIPE)
        out, err = p.communicate()
        # finalizing
        value = time.time() - t0

        os.chdir(def_path)
        return value

    def pre(self):
        pass

    def pos(self):
        pass


if __name__ == '__main__':
    COptimizer().main()
