#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Mojolicious-Plugin-AssetPack
Version  : 2.15
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-Plugin-AssetPack-2.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-Plugin-AssetPack-2.15.tar.gz
Summary  : 'Compress and convert CSS, Less, Sass, JavaScript and CoffeeScript files'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Mojolicious-Plugin-AssetPack-license = %{version}-%{release}
Requires: perl-Mojolicious-Plugin-AssetPack-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::MD5)
BuildRequires : perl(File::Which)
BuildRequires : perl(IPC::Run3)
BuildRequires : perl(Mojo::Base)
BuildRequires : perl(Mojolicious)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Mojolicious::Plugin::AssetPack [![](https://github.com/mojolicious/mojo-assetpack/workflows/linux/badge.svg)](https://github.com/mojolicious/mojo-assetpack/actions)

%package dev
Summary: dev components for the perl-Mojolicious-Plugin-AssetPack package.
Group: Development
Provides: perl-Mojolicious-Plugin-AssetPack-devel = %{version}-%{release}
Requires: perl-Mojolicious-Plugin-AssetPack = %{version}-%{release}

%description dev
dev components for the perl-Mojolicious-Plugin-AssetPack package.


%package license
Summary: license components for the perl-Mojolicious-Plugin-AssetPack package.
Group: Default

%description license
license components for the perl-Mojolicious-Plugin-AssetPack package.


%package perl
Summary: perl components for the perl-Mojolicious-Plugin-AssetPack package.
Group: Default
Requires: perl-Mojolicious-Plugin-AssetPack = %{version}-%{release}

%description perl
perl components for the perl-Mojolicious-Plugin-AssetPack package.


%prep
%setup -q -n Mojolicious-Plugin-AssetPack-2.15
cd %{_builddir}/Mojolicious-Plugin-AssetPack-2.15
pushd ..
cp -a Mojolicious-Plugin-AssetPack-2.15 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojolicious-Plugin-AssetPack
cp %{_builddir}/Mojolicious-Plugin-AssetPack-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojolicious-Plugin-AssetPack/2f8018a02043ed1a43f032379e036bb6b88265f2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mojolicious::Plugin::AssetPack.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Asset.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Asset::Null.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Guides::Cookbook.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Guides::Developing.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Guides::Tutorial.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::CoffeeScript.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Combine.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Css.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Favicon.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Fetch.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::JavaScript.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Jpeg.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Less.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Png.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Riotjs.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::RollupJs.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Sass.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::TypeScript.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Pipe::Vuejs.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Store.3
/usr/share/man/man3/Mojolicious::Plugin::AssetPack::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mojolicious-Plugin-AssetPack/2f8018a02043ed1a43f032379e036bb6b88265f2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
