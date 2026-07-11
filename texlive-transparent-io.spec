%global tl_name transparent-io
%global tl_revision 64113

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Show for approval the filenames used in \input, \openin, or \openout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/transparent-io
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/transparent-io.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/transparent-io.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros to make the file I/O in plain TeX more
transparent. That is, every \input, \openin, and \openout operation by
TeX is presented to the user who must check carefully if the file name
of the source is acceptable. The user must sometimes enter additional
text and has to specify the file name that the TeX operation should use.
The macros require a complex installation procedure; the package
contains sed and bash scripts to do this on a UNIX-like operating
system. Every installation is different from any other as password-
protected macro names and private messages have to be chosen by the
installer. Therefore, the files in the package cannot be used directly.
The files carry the extension .org, and only after the user has
performed an individual customization for a private installation the
changed files are renamed and have the extension .tex. For details see
the manual.

