include check_tools.make

.PHONY: all
all: muscle_manager_protocol ymmsl libmuscle

.PHONY: test
test: tests
	$(MAKE) -C ymmsl test
	$(MAKE) -C libmuscle test

.PHONY: install
install: all protobuf_install grpc_install msgpack_install
	$(MAKE) -C ymmsl install
	$(MAKE) -C libmuscle install

.PHONY: clean
clean:
	$(MAKE) -C msgpack clean
	$(MAKE) -C protobuf clean
	$(MAKE) -C grpc clean
	$(MAKE) -C googletest clean
	$(MAKE) -C muscle_manager_protocol clean
	$(MAKE) -C ymmsl clean
	$(MAKE) -C libmuscle clean

.PHONY: distclean
distclean:
	$(MAKE) -C msgpack distclean
	$(MAKE) -C protobuf distclean
	$(MAKE) -C grpc distclean
	$(MAKE) -C googletest distclean
	$(MAKE) -C muscle_manager_protocol distclean
	$(MAKE) -C ymmsl distclean
	$(MAKE) -C libmuscle distclean

# Find dependencies or set up build

dep_name := protobuf
dep_version_constraint := = 3.10.0
dep_version := 3.10.0
dep_pkgconfig_name := protobuf
dep_install := 1
include $(TOOLDIR)/make_available.make

dep_name := grpc
dep_version_constraint := = 1.24.3
dep_version := 1.24.3
dep_pkgconfig_name := grpc++
dep_install := 1
include $(TOOLDIR)/make_available.make

# If gRPC is available but we're building our own protobuf, then we should
# build our own gRPC as well, linked against our own protobuf, to avoid having
# two versions of protobuf in the same process.
ifeq (grpc_AVAILABLE, 1)
    ifneq (protobuf_AVAILABLE, 1)
        include $(TOOLDIR)/dep_build.make
    endif
endif

grpc: protobuf

dep_name := msgpack
dep_version_constraint := >= 3.1.0
dep_version := 3.2.0
dep_pkgconfig_name := msgpack
dep_install := 1
include $(TOOLDIR)/make_available.make

dep_name := googletest
dep_version_constraint := >= 1.8.1
dep_version := 1.8.1
dep_pkgconfig_name := gtest
dep_install := 0
include $(TOOLDIR)/make_available.make

# Directories where local builds will be available

DEP_DIRS := $(CURDIR)/protobuf/protobuf
DEP_DIRS += $(CURDIR)/grpc/c-ares/c-ares
DEP_DIRS += $(CURDIR)/grpc/openssl/openssl
DEP_DIRS += $(CURDIR)/grpc/zlib/zlib
DEP_DIRS += $(CURDIR)/grpc/grpc
DEP_DIRS += $(CURDIR)/msgpack/msgpack
export DEP_DIRS

PKG_CONFIG_EXTRA_DIRS := $(CURDIR)/protobuf/protobuf/lib/pkgconfig
PKG_CONFIG_EXTRA_DIRS := $(PKG_CONFIG_EXTRA_DIRS):$(CURDIR)/grpc/c-ares/c-ares/lib/pkgconfig
PKG_CONFIG_EXTRA_DIRS := $(PKG_CONFIG_EXTRA_DIRS):$(CURDIR)/grpc/openssl/openssl/lib/pkgconfig
PKG_CONFIG_EXTRA_DIRS := $(PKG_CONFIG_EXTRA_DIRS):$(CURDIR)/grpc/zlib/zlib/lib/pkgconfig
PKG_CONFIG_EXTRA_DIRS := $(PKG_CONFIG_EXTRA_DIRS):$(CURDIR)/grpc/grpc/lib/pkgconfig
PKG_CONFIG_EXTRA_DIRS := $(PKG_CONFIG_EXTRA_DIRS):$(CURDIR)/msgpack/msgpack/lib/pkgconfig
export PKG_CONFIG_EXTRA_DIRS


.PHONY: muscle_manager_protocol
muscle_manager_protocol: grpc protobuf
	@echo
	@echo 'Building muscle manager protocol...'
	$(MAKE) -j $(NCORES) -C muscle_manager_protocol

.PHONY: ymmsl
ymmsl:
	@echo
	@echo 'Building ymmsl...'
	$(MAKE) -j $(NCORES) -C ymmsl


.PHONY: libmuscle
libmuscle: grpc ymmsl msgpack muscle_manager_protocol
	@echo
	@echo 'Building libmuscle...'
	$(MAKE) -j $(NCORES) -C libmuscle


.PHONY: tests
tests: ymmsl libmuscle msgpack muscle_manager_protocol googletest
	$(MAKE) -j $(NCORES) -C ymmsl tests
	$(MAKE) -j $(NCORES) -C libmuscle tests

cpp_test_files := ymmsl/tests/test_* libmuscle/tests/test_*
