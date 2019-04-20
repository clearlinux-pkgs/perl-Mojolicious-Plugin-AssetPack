#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojolicious-Plugin-AssetPack
Version  : 2.06
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Mojolicious-Plugin-AssetPack-2.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Mojolicious-Plugin-AssetPack-2.06.tar.gz
Summary  : 'Compress and convert css, less, sass, javascript and coffeescript files'
Group    : Development/Tools
License  : Artistic-2.0
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Which)
BuildRequires : perl(IPC::Run3)
BuildRequires : perl(Mojo::Base)
BuildRequires : perl(Mojolicious)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Mojolicious-Plugin-AssetPack package.
Group: Development
Provides: perl-Mojolicious-Plugin-AssetPack-devel = %{version}-%{release}

%description dev
dev components for the perl-Mojolicious-Plugin-AssetPack package.


%prep
%setup -q -n Mojolicious-Plugin-AssetPack-2.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Asset.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Asset/Null.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Guides/Cookbook.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Guides/Developing.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Guides/Tutorial.pod
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/CoffeeScript.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Combine.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Css.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Favicon.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Fetch.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/JavaScript.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Jpeg.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Less.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Png.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Riotjs.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/RollupJs.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Sass.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/TypeScript.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/Vuejs.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/require.js
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/riot.js
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Pipe/typescript.js
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Store.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojolicious/Plugin/AssetPack/Util.pm

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
