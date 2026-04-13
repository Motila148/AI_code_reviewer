import {Fragment,useCallback,useContext,useEffect,useRef} from "react"
import {Badge as RadixThemesBadge,Box as RadixThemesBox,Button as RadixThemesButton,Code as RadixThemesCode,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Link as RadixThemesLink,Text as RadixThemesText,TextArea as RadixThemesTextArea} from "@radix-ui/themes"
import {ColorModeContext,EventLoopContext,StateContexts,UploadFilesContext} from "$/utils/context"
import {} from "react-dropzone"
import {ReflexEvent,isTrue,refs} from "$/utils/state"
import {useDropzone} from "react-dropzone"
import DebounceInput from "react-debounce-input"
import ReactMarkdown from "react-markdown"
import remarkMath from "remark-math"
import remarkGfm from "remark-gfm"
import rehypeKatex from "rehype-katex"
import "katex/dist/katex.min.css"
import rehypeRaw from "rehype-raw"
import rehypeUnwrapImages from "rehype-unwrap-images"
import {Link as ReactRouterLink} from "react-router"
import {PrismAsyncLight as SyntaxHighlighter} from "react-syntax-highlighter"
import oneLight from "react-syntax-highlighter/dist/esm/styles/prism/one-light"
import oneDark from "react-syntax-highlighter/dist/esm/styles/prism/one-dark"
import {jsx} from "@emotion/react"




function Heading_8291137bf842a55905044629210b3bba () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.error_count_rx_state_)
  )
}


function Heading_2ebc773f0f6d1525e2f9ecf243366675 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.warning_count_rx_state_)
  )
}


function Heading_b2e8498fa7691c1ccf5c827e51e34d4c () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.info_count_rx_state_)
  )
}


function Heading_245a65dfdeb2cb861a5c01d308496e3f () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.line_count_rx_state_)
  )
}


function Comp_75799ac5aa99c2db73a83928d739c997 () {
  const ref_python_code_upload = useRef(null); refs["ref_python_code_upload"] = ref_python_code_upload;
const [addEvents, connectErrors] = useContext(EventLoopContext);
const [filesById, setFilesById] = useContext(UploadFilesContext);
const on_drop_30adf8e86a77043ec11b0dd4201afa6b = useCallback(e => setFilesById(filesById => {
    const updatedFilesById = Object.assign({}, filesById);
    updatedFilesById["python_code_upload"] = e;
    return updatedFilesById;
  })
    , [addEvents, ReflexEvent, filesById, setFilesById])
const on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => (refs['__toast']?.["error"]("", ({ ["title"] : "Files not Accepted", ["description"] : _ev_0.map(((osizayzf) => (osizayzf?.["file"]?.["path"]+": "+osizayzf?.["errors"].map(((wnkiegyk) => wnkiegyk?.["message"])).join(", ")))).join("\n\n"), ["closeButton"] : true, ["style"] : ({ ["whiteSpace"] : "pre-line" }) })))), ["callback"] : null }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const { getRootProps: xdvxrcsn, getInputProps: udaxihhe, isDragActive: bacghqta} = useDropzone(({ ["accept"] : ({ ["text/plain"] : [".py", ".pyi", ".txt"] }), ["maxFiles"] : 1, ["multiple"] : false, ["id"] : "python_code_upload", ["onDrop"] : on_drop_30adf8e86a77043ec11b0dd4201afa6b, ["onDropRejected"] : on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 }));



  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{className:"rx-Upload",css:({ ["width"] : "100%", ["padding"] : "2.2rem 1rem", ["border"] : "1.5px dashed #94a3b8", ["borderRadius"] : "20px", ["background"] : "linear-gradient(180deg, rgba(255,255,255,0.82) 0%, rgba(241,245,249,0.98) 100%)", ["textAlign"] : "center" }),id:"python_code_upload",ref:ref_python_code_upload,...xdvxrcsn()},jsx("input",{type:"file",...udaxihhe()},),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "1.05rem", ["fontWeight"] : "600", ["color"] : "#0f172a" })},"Drop a .py file here"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#64748b" })},"or click to browse from your machine"))))
  )
}


function Button_84b300cca38afa998abb39d85720f126 () {
  const [filesById, setFilesById] = useContext(UploadFilesContext);
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_4a7f1c48adeb839292af04268b1816c6 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.code_reviewer___state____code_state.handle_upload", ({ ["files"] : filesById?.["python_code_upload"], ["upload_id"] : "python_code_upload", ["extra_headers"] : ({  }) }), ({  }), "uploadFiles"))], [_e], ({  })))), [addEvents, ReflexEvent, filesById, setFilesById])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#1d4ed8", ["color"] : "white", ["borderRadius"] : "999px" }),onClick:on_click_4a7f1c48adeb839292af04268b1816c6},"Load file")
  )
}


function Flex_a385a6853274d5b24e889e94e9758735 () {
  const [filesById, setFilesById] = useContext(UploadFilesContext);



  return (
    jsx(RadixThemesFlex,{align:"center",css:({ ["width"] : "100%", ["gap"] : "0.75rem" }),wrap:"wrap"},Array.prototype.map.call((filesById["python_code_upload"] ? filesById["python_code_upload"].map((f) => f.name) : []) ?? [],((name_rx_state_,index_a5e1a725d11b03436e0aeabd80e8eef7)=>(jsx(RadixThemesBadge,{color:"blue",key:index_a5e1a725d11b03436e0aeabd80e8eef7,radius:"full",size:"3",variant:"soft"},name_rx_state_)))),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},),jsx(Button_84b300cca38afa998abb39d85720f126,{},))
  )
}


function Text_76962e622649ff5eaef24d9110765daf () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#334155", ["fontSize"] : "0.95rem" })},reflex___state____state__code_reviewer___state____code_state.syntax_message_rx_state_)
  )
}


function Debounceinput_9ad4ad25822e42741ee7e3340756f9a3 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_0f9becb0a85f24293137397ed99c8c62 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.code_reviewer___state____code_state.update_code_input", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["minHeight"] : "360px", ["background"] : "#0f172a", ["color"] : "#e2e8f0", ["borderRadius"] : "20px", ["fontFamily"] : "'IBM Plex Mono', 'Consolas', monospace", ["--default-font-family"] : "'IBM Plex Mono', 'Consolas', monospace", ["padding"] : "1rem" }),debounceTimeout:300,element:RadixThemesTextArea,onChange:on_change_0f9becb0a85f24293137397ed99c8c62,placeholder:"Paste Python code here if you do not want to upload a file.",resize:"vertical",value:reflex___state____state__code_reviewer___state____code_state.code_input_rx_state_},)
  )
}


function Button_983ec53b44f583bcba98e04556a3309b () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_316058ac571b0d231276c2b54a660095 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.code_reviewer___state____code_state.analyze", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#c2410c", ["color"] : "white", ["borderRadius"] : "999px" }),loading:reflex___state____state__code_reviewer___state____code_state.is_loading_rx_state_,onClick:on_click_316058ac571b0d231276c2b54a660095,size:"3"},"Analyze code")
  )
}


function Button_23ee7bccf5527d5f094bc1ac08a07767 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_148645846aa8513c78b5c51d33d90b6a = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.code_reviewer___state____code_state.load_sample", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{color:"amber",css:({ ["borderRadius"] : "999px" }),onClick:on_click_148645846aa8513c78b5c51d33d90b6a,size:"3",variant:"soft"},"Load sample")
  )
}


function Button_fe9dd8262119ec03c6d8cbf6ed31efc1 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_309b5f02a140b4cb1ca24fb145bbc8fb = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.code_reviewer___state____code_state.clear_workspace", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{color:"gray",css:({ ["borderRadius"] : "999px" }),onClick:on_click_309b5f02a140b4cb1ca24fb145bbc8fb,size:"3",variant:"outline"},"Clear")
  )
}


function Text_e86df54135868a8bf537756361fd2f35 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#991b1b", ["fontWeight"] : "600" })},reflex___state____state__code_reviewer___state____code_state.error_message_rx_state_)
  )
}


function Fragment_4e7cd824d2ede8929dc1f535a21cd608 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__code_reviewer___state____code_state.error_message_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "0.9rem 1rem", ["borderRadius"] : "16px", ["background"] : "#fef2f2", ["border"] : "1px solid #fecaca", ["width"] : "100%" })},jsx(Text_e86df54135868a8bf537756361fd2f35,{},)))):(jsx(Fragment,{},))))
  )
}


function Text_14e74f21da7681b2d66b186b0c7bfc85 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#0f172a", ["fontWeight"] : "500" })},reflex___state____state__code_reviewer___state____code_state.review_summary_rx_state_)
  )
}


function Heading_04d1044573a894821fa3aff022d28b48 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.non_empty_lines_rx_state_)
  )
}


function Heading_e971829928043da29d56f62f1ee4c588 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.function_count_rx_state_)
  )
}


function Heading_bb83c7647ec211f6a4a093e27c6d842d () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.class_count_rx_state_)
  )
}


function Heading_acfda2ed3808bf8c8dc9db29e3c25071 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a" }),size:"7"},reflex___state____state__code_reviewer___state____code_state.import_count_rx_state_)
  )
}


function Flex_192d8e32b347245c626d6fa9c4a2053e () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},Array.prototype.map.call(reflex___state____state__code_reviewer___state____code_state.findings_rx_state_ ?? [],((finding_rx_state_,index_10a63532471ed8c3295efa7e8bdc97ee)=>(jsx(RadixThemesBox,{css:({ ["padding"] : "0.9rem 1rem", ["borderRadius"] : "16px", ["background"] : "#f8fafc", ["border"] : "1px solid #e2e8f0", ["width"] : "100%" }),key:index_10a63532471ed8c3295efa7e8bdc97ee},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#0f172a", ["whiteSpace"] : "pre-wrap", ["lineHeight"] : "1.55" })},finding_rx_state_))))))
  )
}


function Fragment_75eb853b1d961451a4f3639ab963d118 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(Fragment,{},(reflex___state____state__code_reviewer___state____code_state.has_findings_rx_state_?(jsx(Fragment,{},jsx(Flex_192d8e32b347245c626d6fa9c4a2053e,{},))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "1rem", ["borderRadius"] : "16px", ["background"] : "#ecfdf5", ["border"] : "1px solid #bbf7d0" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#166534", ["fontWeight"] : "600" })},"No static findings were reported for this file."))))))
  )
}


function Badge_848d76ae2c90288042d01c67d61b9f9e () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesBadge,{color:"indigo",radius:"full",size:"3",variant:"soft"},reflex___state____state__code_reviewer___state____code_state.llm_status_rx_state_)
  )
}


function Badge_bbba2cf54eb92bccc3b1226835dd3ac8 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesBadge,{color:"cyan",radius:"full",size:"3",variant:"soft"},reflex___state____state__code_reviewer___state____code_state.llm_provider_rx_state_)
  )
}


        function ComponentMap_d59534cfa3df3086665270d8af3d1699 () {
            const { resolvedColorMode } = useContext(ColorModeContext)



            return (
                ({ ["h1"] : (({node, children, ...props}) => (jsx(RadixThemesHeading,{as:"h1",css:({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" }),size:"6",...props},children))), ["h2"] : (({node, children, ...props}) => (jsx(RadixThemesHeading,{as:"h2",css:({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" }),size:"5",...props},children))), ["h3"] : (({node, children, ...props}) => (jsx(RadixThemesHeading,{as:"h3",css:({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" }),size:"4",...props},children))), ["h4"] : (({node, children, ...props}) => (jsx(RadixThemesHeading,{as:"h4",css:({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" }),size:"3",...props},children))), ["h5"] : (({node, children, ...props}) => (jsx(RadixThemesHeading,{as:"h5",css:({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" }),size:"2",...props},children))), ["h6"] : (({node, children, ...props}) => (jsx(RadixThemesHeading,{as:"h6",css:({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" }),size:"1",...props},children))), ["p"] : (({node, children, ...props}) => (jsx(RadixThemesText,{as:"p",css:({ ["marginTop"] : "1em", ["marginBottom"] : "1em" }),...props},children))), ["ul"] : (({node, children, ...props}) => (jsx("ul",{css:({ ["listStyleType"] : "disc", ["marginTop"] : "1em", ["marginBottom"] : "1em", ["marginLeft"] : "1.5rem", ["direction"] : "column" }),...props},children))), ["ol"] : (({node, children, ...props}) => (jsx("ol",{css:({ ["listStyleType"] : "decimal", ["marginTop"] : "1em", ["marginBottom"] : "1em", ["marginLeft"] : "1.5rem", ["direction"] : "column" }),...props},children))), ["li"] : (({node, children, ...props}) => (jsx("li",{css:({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" }),...props},children))), ["a"] : (({node, children, ...props}) => (jsx(RadixThemesLink,{css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),href:"#",...props},children))), ["code"] : (({node, children, ...props}) => (jsx(RadixThemesCode,{...props},children))), ["pre"] : (({node, ...rest}) => { const {node: childNode, className, children: components, ...props} = rest.children.props; const children = String(Array.isArray(components) ? components.join('\n') : components).replace(/\n$/, ''); const match = (className || '').match(/language-(?<lang>.*)/); let _language = match ? match[1] : ''; ;             return jsx(SyntaxHighlighter,{children:children,css:({ ["marginTop"] : "1em", ["marginBottom"] : "1em" }),language:_language,style:((resolvedColorMode?.valueOf?.() === "light"?.valueOf?.()) ? oneLight : oneDark),wrapLongLines:true,...props},);         }) })
            )
        }
        

function Reactmarkdown_8b01a8af794aa8ef167ef3d628ba7d25 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(ReactMarkdown,{components:ComponentMap_d59534cfa3df3086665270d8af3d1699(),rehypePlugins:[rehypeKatex, rehypeRaw, rehypeUnwrapImages],remarkPlugins:[remarkMath, remarkGfm]},reflex___state____state__code_reviewer___state____code_state.llm_review_rx_state_)
  )
}


function Textarea_9d26ea8cbb3c795c5939e045e6e2111b () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesTextArea,{css:({ ["& textarea"] : ({ ["padding"] : "1rem" }), ["width"] : "100%", ["minHeight"] : "420px", ["background"] : "#020617", ["color"] : "#e2e8f0", ["border"] : "1px solid #1d4ed8", ["borderRadius"] : "18px", ["fontFamily"] : "'IBM Plex Mono', 'Consolas', monospace", ["--default-font-family"] : "'IBM Plex Mono', 'Consolas', monospace" }),readOnly:true,resize:"vertical",value:reflex___state____state__code_reviewer___state____code_state.code_input_rx_state_},)
  )
}


function Textarea_17f38f067e333e6251ed0b832f73b328 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(RadixThemesTextArea,{css:({ ["& textarea"] : ({ ["padding"] : "1rem" }), ["width"] : "100%", ["minHeight"] : "420px", ["background"] : "#020617", ["color"] : "#e2e8f0", ["border"] : "1px solid #c2410c", ["borderRadius"] : "18px", ["fontFamily"] : "'IBM Plex Mono', 'Consolas', monospace", ["--default-font-family"] : "'IBM Plex Mono', 'Consolas', monospace" }),readOnly:true,resize:"vertical",value:reflex___state____state__code_reviewer___state____code_state.corrected_code_rx_state_},)
  )
}


function Fragment_5b8d2fc3bd50fe5db357bd576076ade6 () {
  const reflex___state____state__code_reviewer___state____code_state = useContext(StateContexts.reflex___state____state__code_reviewer___state____code_state)



  return (
    jsx(Fragment,{},(reflex___state____state__code_reviewer___state____code_state.review_ready_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"5"},jsx(RadixThemesBox,{css:({ ["padding"] : "1.35rem", ["borderRadius"] : "24px", ["background"] : "rgba(255, 255, 255, 0.9)", ["border"] : "1px solid rgba(148, 163, 184, 0.22)", ["boxShadow"] : "0 18px 48px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesBox,{css:({ ["spacing"] : "1", ["width"] : "100%" })},jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a", ["fontFamily"] : "'Space Grotesk', 'Trebuchet MS', sans-serif", ["--default-font-family"] : "'Space Grotesk', 'Trebuchet MS', sans-serif" }),size:"6"},"Static Review"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#475569", ["fontSize"] : "0.95rem" })},"Local analysis combines AST checks, syntax parsing, and lightweight PEP-oriented rules.")),jsx(Text_14e74f21da7681b2d66b186b0c7bfc85,{},),jsx(RadixThemesFlex,{css:({ ["width"] : "100%" }),gap:"4",wrap:"wrap"},jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #dbeafe", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Non-empty lines"),jsx(Heading_04d1044573a894821fa3aff022d28b48,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #fde68a", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Functions"),jsx(Heading_e971829928043da29d56f62f1ee4c588,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #c7d2fe", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Classes"),jsx(Heading_bb83c7647ec211f6a4a093e27c6d842d,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #fecdd3", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Imports"),jsx(Heading_acfda2ed3808bf8c8dc9db29e3c25071,{},))),jsx(Fragment_75eb853b1d961451a4f3639ab963d118,{},))),jsx(RadixThemesBox,{css:({ ["padding"] : "1.35rem", ["borderRadius"] : "24px", ["background"] : "rgba(255, 255, 255, 0.9)", ["border"] : "1px solid rgba(148, 163, 184, 0.22)", ["boxShadow"] : "0 18px 48px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesBox,{css:({ ["spacing"] : "1", ["width"] : "100%" })},jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a", ["fontFamily"] : "'Space Grotesk', 'Trebuchet MS', sans-serif", ["--default-font-family"] : "'Space Grotesk', 'Trebuchet MS', sans-serif" }),size:"6"},"LLM Review"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#475569", ["fontSize"] : "0.95rem" })},"The model now returns both analysis and a corrected version of the code.")),jsx(RadixThemesFlex,{css:({ ["gap"] : "0.75rem" }),wrap:"wrap"},jsx(Badge_848d76ae2c90288042d01c67d61b9f9e,{},),jsx(Badge_bbba2cf54eb92bccc3b1226835dd3ac8,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "1rem", ["borderRadius"] : "18px", ["background"] : "#f8fafc", ["border"] : "1px solid #e2e8f0", ["width"] : "100%" })},jsx("div",{},jsx(Reactmarkdown_8b01a8af794aa8ef167ef3d628ba7d25,{},))),jsx(RadixThemesFlex,{align:"stretch",css:({ ["gap"] : "1rem", ["width"] : "100%" }),direction:"row",wrap:"wrap"},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#334155", ["fontWeight"] : "600", ["fontSize"] : "0.95rem" })},"Input code"),jsx(Textarea_9d26ea8cbb3c795c5939e045e6e2111b,{},)),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#334155", ["fontWeight"] : "600", ["fontSize"] : "0.95rem" })},"LLM corrected code"),jsx(Textarea_17f38f067e333e6251ed0b832f73b328,{},)))))))):(jsx(Fragment,{},))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "1.2rem 1.6rem", ["background"] : "rgba(248, 250, 252, 0.92)", ["borderBottom"] : "1px solid rgba(148, 163, 184, 0.18)", ["backdropFilter"] : "blur(14px)" })},jsx(RadixThemesFlex,{align:"center",css:({ ["width"] : "100%" }),justify:"between"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a", ["fontFamily"] : "'Manrope', 'Trebuchet MS', sans-serif", ["--default-font-family"] : "'Manrope', 'Trebuchet MS', sans-serif" }),size:"7"},"Code Review Studio"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#475569", ["fontSize"] : "0.96rem" })},"Production-style review workspace for Python analysis and cleanups.")),jsx(RadixThemesBox,{css:({ ["padding"] : "0.55rem 0.9rem", ["borderRadius"] : "999px", ["background"] : "rgba(255, 255, 255, 0.88)", ["border"] : "1px solid rgba(148, 163, 184, 0.28)" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#0f172a", ["fontWeight"] : "600", ["fontSize"] : "0.88rem" })},"Live Review")))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["minHeight"] : "100vh", ["padding"] : "1.5rem", ["background"] : "radial-gradient(circle at top left, rgba(251, 191, 36, 0.18), transparent 32%), radial-gradient(circle at top right, rgba(59, 130, 246, 0.16), transparent 28%), linear-gradient(180deg, #fff8ef 0%, #f8fafc 46%, #eef2ff 100%)" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["maxWidth"] : "1120px" }),direction:"column",gap:"5"},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "1.8rem", ["borderRadius"] : "28px", ["background"] : "linear-gradient(135deg, rgba(180, 83, 9, 0.92) 0%, rgba(194, 65, 12, 0.88) 38%, rgba(30, 64, 175, 0.88) 100%)", ["boxShadow"] : "0 26px 65px rgba(30, 41, 59, 0.18)" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesBadge,{color:"orange",radius:"full",size:"3",variant:"soft"},"Static review + model review"),jsx(RadixThemesHeading,{css:({ ["color"] : "#fff7ed", ["fontFamily"] : "'Space Grotesk', 'Trebuchet MS', sans-serif", ["--default-font-family"] : "'Space Grotesk', 'Trebuchet MS', sans-serif", ["lineHeight"] : "1.1" }),size:"8"},"Upload Python code, catch structural issues, then send the clean context to an LLM."),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#ffedd5", ["fontSize"] : "1rem", ["maxWidth"] : "54rem", ["lineHeight"] : "1.7" })},"This reviewer parses code with Python AST, flags syntax and probable logic problems, checks a few PEP-style rules, and then asks a language model for higher-level analysis."))),jsx(RadixThemesFlex,{css:({ ["width"] : "100%" }),gap:"4",wrap:"wrap"},jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #fecaca", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Errors"),jsx(Heading_8291137bf842a55905044629210b3bba,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #fed7aa", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Warnings"),jsx(Heading_2ebc773f0f6d1525e2f9ecf243366675,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #bfdbfe", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Notes"),jsx(Heading_b2e8498fa7691c1ccf5c827e51e34d4c,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "1rem 1.1rem", ["borderRadius"] : "18px", ["background"] : "rgba(255, 255, 255, 0.82)", ["border"] : "1px solid #cbd5e1", ["boxShadow"] : "0 16px 38px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.82rem", ["textTransform"] : "uppercase", ["letterSpacing"] : "0.08em", ["color"] : "#64748b" })},"Lines"),jsx(Heading_245a65dfdeb2cb861a5c01d308496e3f,{},))),jsx(RadixThemesBox,{css:({ ["padding"] : "1.35rem", ["borderRadius"] : "24px", ["background"] : "rgba(255, 255, 255, 0.9)", ["border"] : "1px solid rgba(148, 163, 184, 0.22)", ["boxShadow"] : "0 18px 48px rgba(15, 23, 42, 0.08)", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesBox,{css:({ ["spacing"] : "1", ["width"] : "100%" })},jsx(RadixThemesHeading,{css:({ ["color"] : "#0f172a", ["fontFamily"] : "'Space Grotesk', 'Trebuchet MS', sans-serif", ["--default-font-family"] : "'Space Grotesk', 'Trebuchet MS', sans-serif" }),size:"6"},"Input"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#475569", ["fontSize"] : "0.95rem" })},"Choose a Python file or paste source directly into the editor.")),jsx(Comp_75799ac5aa99c2db73a83928d739c997,{},),jsx(Flex_a385a6853274d5b24e889e94e9758735,{},),jsx(Text_76962e622649ff5eaef24d9110765daf,{},),jsx(Debounceinput_9ad4ad25822e42741ee7e3340756f9a3,{},),jsx(RadixThemesFlex,{css:({ ["gap"] : "0.75rem" }),wrap:"wrap"},jsx(Button_983ec53b44f583bcba98e04556a3309b,{},),jsx(Button_23ee7bccf5527d5f094bc1ac08a07767,{},),jsx(Button_fe9dd8262119ec03c6d8cbf6ed31efc1,{},)),jsx(Fragment_4e7cd824d2ede8929dc1f535a21cd608,{},))),jsx(Fragment_5b8d2fc3bd50fe5db357bd576076ade6,{},)))),jsx("title",{},"AI Code Reviewer"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}