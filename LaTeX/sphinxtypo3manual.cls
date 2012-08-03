%%
%% This is file `sphinxtypo3manual.cls'
%%
%% Copyright (c) 2011-2012 Xavier Perseguers <xavier@typo3.org>
%%
\ProvidesClass{sphinxtypo3manual}[2012/08/03 v.0.2
  TYPO3 Manual]
\NeedsTeXFormat{LaTeX2e}[1995/06/01]
\LoadClass[a4paper,11pt,twoside]{article}
% For graphicx, check if we are compiling under latex or pdflatex.
\ifx\pdftexversion\undefined
  \RequirePackage{graphicx}
\else
  \RequirePackage[pdftex]{graphicx}
\fi
\RequirePackage{geometry,tabularx,multicol,colortbl}
\RequirePackage[english]{babel}
\RequirePackage{fancyhdr}
\RequirePackage[utf8]{inputenc}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\RequirePackage[T1]{fontenc}

\ProcessOptions

%% Setting proper dimensions
\geometry{margin=2.5cm}

%% TYPO3 font
\newcommand\sharefont{\fontfamily{typo3share}\selectfont}

\pagestyle{fancy}
%% with this we ensure that the chapter and section
%% headings are in lowercase.
\renewcommand{\sectionmark}[1]{\markboth{#1}{}}
\renewcommand{\subsectionmark}[1]{\markright{\thesection.\ #1}}
\fancyhf{}          % delete current setting for header and footer
\fancyhead[LE,RO]{\sharefont\bfseries\thepage}
\fancyhead[LO]{\sharefont\bfseries\hspace{-0em}\rightmark}
\fancyhead[RE]{\sharefont\bfseries\leftmark}
\fancyfoot[LE]{\origincludegraphics[height=.4cm]{typo3_logo_color}}
\fancyfoot[RO]{%
	\sharefont inspiring people to \textbf{\emph{share}}.%
	\quad%
	\origincludegraphics[height=.4cm]{typo3_logo_color}%
}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0pt}
\addtolength{\headheight}{2.34pt} % make space for the rule
\fancypagestyle{plain}{
  \fancyhead{}      % get rid of headers on plain pages
  \renewcommand{\headrulewidth}{0pt} % and the line
}

%% Change font for sections
\makeatletter
\renewcommand\section{\@startsection {section}{1}{\z@}%
	{-3.5ex \@plus -1ex \@minus -.2ex}%
	{2.3ex \@plus.2ex}%
	{\normalfont\sharefont\Large\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
	{-3.25ex\@plus -1ex \@minus -.2ex}%
	{1.5ex \@plus .2ex}%
	{\normalfont\sharefont\large\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
	{-3.25ex\@plus -1ex \@minus -.2ex}%
	{1.5ex \@plus .2ex}%
	{\normalfont\sharefont\normalsize\bfseries}}
\makeatother

%% Automatically scale down graphics if too large
\makeatletter
\def\maxwidth{%
  \ifdim.5\Gin@nat@width>\linewidth
    \linewidth
  \else
    .5\Gin@nat@width
  \fi
}
\makeatother
\let\origincludegraphics=\includegraphics
\renewcommand{\includegraphics}[1]{\origincludegraphics[width=\maxwidth]{#1}}

%% Do not \vfill on pages that LaTeX cannot fill properly
\raggedbottom

%% Make sure not to show too many nested levels
\setcounter{tocdepth}{2}
\makeatletter
\renewcommand{\tableofcontents}{%
	\section*{\contentsname}
	\begin{multicols}{2}
	\small
	\@starttoc{toc}%
	\end{multicols}
}
\makeatother

\endinput
%%
%% End of file `sphinxtypo3manual.cls'.
