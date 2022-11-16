Name:		texlive-transparent-io
Version:	64113
Release:	1
Summary:	Show for approval the filenames used in \input, \openin, or \openout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/transparent-io
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/transparent-io.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/transparent-io.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros to make the file I/O in plain TeX
more transparent. That is, every \input, \openin, and \openout
operation by TeX is presented to the user who must check
carefully if the file name of the source is acceptable. The
user must sometimes enter additional text and has to specify
the file name that the TeX operation should use. The macros
require a complex installation procedure; the package contains
sed and bash scripts to do this on a UNIX-like operating
system. Every installation is different from any other as
password-protected macro names and private messages have to be
chosen by the installer. Therefore, the files in the package
cannot be used directly. The files carry the extension .org,
and only after the user has performed an individual
customization for a private installation the changed files are
renamed and have the extension .tex. For details see the
manual.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/plain/transparent-io

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
