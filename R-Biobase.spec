#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-Biobase
Version  : 2.64.0
Release  : 1
URL      : https://bioconductor.org/packages/release/bioc/src/contrib/Biobase_2.64.0.tar.gz
Source0  : https://bioconductor.org/packages/release/bioc/src/contrib/Biobase_2.64.0.tar.gz
Summary  : Biobase: Base functions for Bioconductor
Group    : Development/Tools
License  : @@ Artistic-2.0
Requires: R-Biobase-lib = %{version}-%{release}
Requires: R-BiocGenerics
BuildRequires : R-BiocGenerics
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
replace R functions.

%package lib
Summary: lib components for the R-Biobase package.
Group: Libraries

%description lib
lib components for the R-Biobase package.


%prep
%setup -q -n Biobase

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724349976

%install
export SOURCE_DATE_EPOCH=1724349976
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Biobase/CITATION
/usr/lib64/R/library/Biobase/Code/DESCRIPTION
/usr/lib64/R/library/Biobase/Code/R/get@PKGNAME@.R
/usr/lib64/R/library/Biobase/Code/man/@PKGNAME@.Rd
/usr/lib64/R/library/Biobase/Code/man/get@PKGNAME@.Rd
/usr/lib64/R/library/Biobase/DESCRIPTION
/usr/lib64/R/library/Biobase/ExpressionSet/DESCRIPTION
/usr/lib64/R/library/Biobase/ExpressionSet/man/@PKGNAME@.Rd
/usr/lib64/R/library/Biobase/INDEX
/usr/lib64/R/library/Biobase/Meta/Rd.rds
/usr/lib64/R/library/Biobase/Meta/data.rds
/usr/lib64/R/library/Biobase/Meta/features.rds
/usr/lib64/R/library/Biobase/Meta/hsearch.rds
/usr/lib64/R/library/Biobase/Meta/links.rds
/usr/lib64/R/library/Biobase/Meta/nsInfo.rds
/usr/lib64/R/library/Biobase/Meta/package.rds
/usr/lib64/R/library/Biobase/Meta/vignette.rds
/usr/lib64/R/library/Biobase/NAMESPACE
/usr/lib64/R/library/Biobase/NEWS
/usr/lib64/R/library/Biobase/R/Biobase
/usr/lib64/R/library/Biobase/R/Biobase.rdb
/usr/lib64/R/library/Biobase/R/Biobase.rdx
/usr/lib64/R/library/Biobase/data/SW.rda
/usr/lib64/R/library/Biobase/data/aaMap.R
/usr/lib64/R/library/Biobase/data/geneCov.R
/usr/lib64/R/library/Biobase/data/geneCovariate.rda
/usr/lib64/R/library/Biobase/data/geneData.R
/usr/lib64/R/library/Biobase/data/reporter.rda
/usr/lib64/R/library/Biobase/data/sample.ExpressionSet.rda
/usr/lib64/R/library/Biobase/data/sample.MultiSet.rda
/usr/lib64/R/library/Biobase/data/seD.rda
/usr/lib64/R/library/Biobase/doc/BiobaseDevelopment.R
/usr/lib64/R/library/Biobase/doc/BiobaseDevelopment.Rmd
/usr/lib64/R/library/Biobase/doc/BiobaseDevelopment.html
/usr/lib64/R/library/Biobase/doc/ExpressionSetIntroduction.R
/usr/lib64/R/library/Biobase/doc/ExpressionSetIntroduction.Rnw
/usr/lib64/R/library/Biobase/doc/ExpressionSetIntroduction.pdf
/usr/lib64/R/library/Biobase/doc/esApply.R
/usr/lib64/R/library/Biobase/doc/esApply.Rmd
/usr/lib64/R/library/Biobase/doc/esApply.html
/usr/lib64/R/library/Biobase/doc/index.html
/usr/lib64/R/library/Biobase/extdata/exprsData.txt
/usr/lib64/R/library/Biobase/extdata/pData.txt
/usr/lib64/R/library/Biobase/help/AnIndex
/usr/lib64/R/library/Biobase/help/Biobase.rdb
/usr/lib64/R/library/Biobase/help/Biobase.rdx
/usr/lib64/R/library/Biobase/help/aliases.rds
/usr/lib64/R/library/Biobase/help/paths.rds
/usr/lib64/R/library/Biobase/html/00Index.html
/usr/lib64/R/library/Biobase/html/R.css
/usr/lib64/R/library/Biobase/scripts/esetTesting.R
/usr/lib64/R/library/Biobase/scripts/getBioC.R
/usr/lib64/R/library/Biobase/scripts/getBioCHelp
/usr/lib64/R/library/Biobase/scripts/getBioCPkgNames.R
/usr/lib64/R/library/Biobase/scripts/makeExpressionSetPackage.R
/usr/lib64/R/library/Biobase/scripts/query.packages.R
/usr/lib64/R/library/Biobase/testClass.R
/usr/lib64/R/library/Biobase/tests/test-all.R
/usr/lib64/R/library/Biobase/tests/test-rowMedians.R
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/1.8/AnnotatedDataFrame.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/1.8/ExpressionSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/1.8/MIAME.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/1.8/exprSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/1.8/phenoData.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/AnnotatedDataFrame.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/ExpressionSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/MIAME.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/MultiSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/ScalarCharacter.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/SnpSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/Versioned.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/VersionedBiobase.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/Versions.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/VersionsNull.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/aggregator.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/container.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/exprSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/2.0/phenoData.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/AnnotatedDataFrame.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/ExpressionSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/MIAME.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/MultiSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/NChannelSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/SWPD.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/ScalarCharacter.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/ScalarInteger.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/ScalarLogical.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/ScalarNumeric.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/SnpSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/Versioned.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/VersionedBiobase.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/Versions.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/VersionsNull.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/aggregator.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/bbsym.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/container.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/eset.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/exprSet.Rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/golubMergeSub.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/sample.eSet.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/sample.exprSet.1.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/sample.exprSet.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/devel/swrep.rda
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/raw/exprs.tab
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/raw/pData.tab
/usr/lib64/R/library/Biobase/unitTests/VersionedClass_data/raw/varMetadata.tab
/usr/lib64/R/library/Biobase/unitTests/test_AnnotatedDataFrame.R
/usr/lib64/R/library/Biobase/unitTests/test_AssayData.R
/usr/lib64/R/library/Biobase/unitTests/test_DataClasses.R
/usr/lib64/R/library/Biobase/unitTests/test_EsetSubclasses.R
/usr/lib64/R/library/Biobase/unitTests/test_ExpressionSet.R
/usr/lib64/R/library/Biobase/unitTests/test_NChannelSet.R
/usr/lib64/R/library/Biobase/unitTests/test_SnpSet.R
/usr/lib64/R/library/Biobase/unitTests/test_UpdateObject.R
/usr/lib64/R/library/Biobase/unitTests/test_VersionedClass.R
/usr/lib64/R/library/Biobase/unitTests/test_cache.R
/usr/lib64/R/library/Biobase/unitTests/test_checkClass.R
/usr/lib64/R/library/Biobase/unitTests/test_combine.R
/usr/lib64/R/library/Biobase/unitTests/test_copyEnv.R
/usr/lib64/R/library/Biobase/unitTests/test_esApply.R
/usr/lib64/R/library/Biobase/unitTests/test_subListExtract.R
/usr/lib64/R/library/Biobase/unitTests/test_unsaveSetSlot.R
/usr/lib64/R/library/Biobase/unitTests/utilities.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Biobase/libs/Biobase.so