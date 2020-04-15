# Placeholders for machine specific flags
# ADDITIONAL_CXX_FLAGS = -I/opt/intel/tbb/include
# ADDITIONAL_LINKFLAGS = -L/opt/intel/tbb/lib/intel64_lin/gcc4.7

#ADDITIONAL_CXX_FLAGS = -W -Wall -pedantic -Wno-strict-aliasing -Woverflow -Werror -Wno-unused -Wno-unused-parameter

uname_p = $(shell uname -p)

# Choice of compiler
ifneq (,$(findstring icc,${CXX}))
  CXX = icc
else
ifneq (,$(findstring clang,${CXX}))
  # Note: When compiling with clang: http://www.agner.org/optimize/vectorclass/read.php?i=89
  CXX = clang++
else
  CXX = g++
endif
endif

# Tune options
ifeq ($(TUNE),) # If TUNE is already set, do nothing
ifeq ($(strip $(uname_p)), aarch64) #arm
	TUNE = -march=armv8-a+simd -ftree-vectorize
else
ifneq (,$(findstring icc,${CXX}))
  TUNE = -xCOMMON-AVX512 -mtune=skylake -no-inline-max-size
#	TUNE = -xMIC-AVX512 -no-inline-max-size
else
ifeq ($(strip $(uname_p)),ppc64le) #ibm
  TUNE = -maltivec -mtune=native -mcpu=native -mfloat128
 # -mvsx -mabi=altivec
else
	TUNE = -march=native
endif
endif
endif
endif

# Choice of vectorization backend (VCL, UMESIMD, NONE)
ifeq ($(strip $(shell echo $(VECTOR_BACKEND) | tr A-Z a-z)), none) 
  DEF_VEC_BACKEND = -DNO_VECTOR_BACKEND
else
ifeq ($(strip $(shell echo $(VECTOR_BACKEND) | tr A-Z a-z)), vcl) 
	DEF_VEC_BACKEND = -DUSE_VCL
else
	DEF_VEC_BACKEND = -DUSE_UMESIMD
endif
endif

# Choice of precision
ifeq ($(strip $(shell echo $(PRECISION) | tr A-Z a-z)), single) 
	DEF_PRECISION = -DSP
else
	DEF_PRECISION = -DDP
endif

# Static vector width
ifeq ($(STATIC_VECTOR_WIDTH),)
  DEF_STATIC_VECTOR_WIDTH = 
else
  DEF_STATIC_VECTOR_WIDTH = -DSTATIC_VECTOR_WIDTH=${STATIC_VECTOR_WIDTH}
endif

TARGET = cross_kalman
CXXFLAGS = -g -std=c++14 ${TUNE} ${DEF_VEC_BACKEND} ${DEF_STATIC_VECTOR_WIDTH} ${DEF_PRECISION} ${ADDITIONAL_CXX_FLAGS}
#LINKFLAGS = -ltbb -lrt ${ADDITIONAL_LINKFLAGS}
OPTIMIZATION = -DNDEBUG -DTBB_OFF
#DEBUG_VARS = -DDEBUG -DTBB_OFF
SOURCES = main.cpp utilities/Instance.cpp utilities/Compare.cpp utilities/Print.cpp
OBJECTS = $(SOURCES:.cpp=.o)

$(TARGET): CXXFLAGS += ${OPTIMIZATION}
$(TARGET): executable

debug: CXXFLAGS += ${DEBUG_VARS}
debug: executable

executable: $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET) $(LINKFLAGS)

.cpp.o:
	$(CXX) -c $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(OBJECTS) $(TARGET)


