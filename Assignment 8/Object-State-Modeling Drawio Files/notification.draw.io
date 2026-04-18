<mxfile host="Electron" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/29.6.1 Chrome/142.0.7444.265 Electron/39.8.0 Safari/537.36" version="29.6.1">
  <diagram name="Page-1" id="LoDP7AoCIoDN9NYEXEwv">
    <mxGraphModel dx="1042" dy="658" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="F6emADJ4_j-nZkKa8t7v-6" edge="1" parent="1" source="F6emADJ4_j-nZkKa8t7v-5" style="endArrow=open;html=1;rounded=0;align=center;verticalAlign=top;endFill=0;labelBackgroundColor=none;endSize=6;" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="440" y="160" as="sourcePoint" />
            <mxPoint x="440" y="240" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-7" edge="1" parent="1" style="endArrow=open;html=1;rounded=0;align=center;verticalAlign=top;endFill=0;labelBackgroundColor=none;endSize=6;" target="F6emADJ4_j-nZkKa8t7v-5" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="440" y="160" as="sourcePoint" />
            <mxPoint x="440" y="280" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-5" parent="1" style="ellipse;html=1;fillColor=#000000;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="430" y="140" as="geometry" />
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-8" parent="1" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="Queued&amp;nbsp;" vertex="1">
          <mxGeometry height="40" width="120" x="380" y="240" as="geometry" />
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-28" parent="1" style="shape=umlFrame;whiteSpace=wrap;html=1;pointerEvents=0;recursiveResize=0;container=1;collapsible=0;width=160;" value="Notification" vertex="1">
          <mxGeometry height="579" width="653" x="158" y="86" as="geometry" />
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-52" parent="F6emADJ4_j-nZkKa8t7v-28" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="Failed" vertex="1">
          <mxGeometry height="40" width="120" x="427" y="283" as="geometry" />
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-61" edge="1" parent="F6emADJ4_j-nZkKa8t7v-28" source="F6emADJ4_j-nZkKa8t7v-8" style="endArrow=open;html=1;rounded=0;align=center;verticalAlign=top;endFill=0;labelBackgroundColor=none;endSize=6;exitX=1;exitY=0.5;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;curved=1;" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="363" y="169" as="sourcePoint" />
            <mxPoint x="486" y="283" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-62" connectable="0" parent="F6emADJ4_j-nZkKa8t7v-61" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="retry [max 3 attempts]" vertex="1">
          <mxGeometry relative="1" x="0.2316" y="1" as="geometry">
            <mxPoint x="-18" y="33" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-10" parent="F6emADJ4_j-nZkKa8t7v-28" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="Sent" vertex="1">
          <mxGeometry height="40" width="118" x="89" y="291" as="geometry" />
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-27" parent="F6emADJ4_j-nZkKa8t7v-28" style="ellipse;html=1;shape=endState;fillColor=strokeColor;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="292" y="452" as="geometry" />
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-55" edge="1" parent="F6emADJ4_j-nZkKa8t7v-28" source="F6emADJ4_j-nZkKa8t7v-52" style="endArrow=open;html=1;rounded=0;align=center;verticalAlign=top;endFill=0;labelBackgroundColor=none;endSize=6;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;curved=1;" target="F6emADJ4_j-nZkKa8t7v-27" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="343" y="743" as="sourcePoint" />
            <mxPoint x="345" y="835" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-77" edge="1" parent="F6emADJ4_j-nZkKa8t7v-28" source="F6emADJ4_j-nZkKa8t7v-10" style="endArrow=open;html=1;rounded=0;align=center;verticalAlign=top;endFill=0;labelBackgroundColor=none;endSize=6;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=0.25;exitY=1;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;curved=1;" target="F6emADJ4_j-nZkKa8t7v-27" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="88" y="317" as="sourcePoint" />
            <mxPoint x="-105" y="456" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-9" edge="1" parent="1" source="F6emADJ4_j-nZkKa8t7v-8" style="endArrow=open;html=1;rounded=0;align=center;verticalAlign=top;endFill=0;labelBackgroundColor=none;endSize=6;edgeStyle=orthogonalEdgeStyle;curved=1;entryX=0.25;entryY=0;entryDx=0;entryDy=0;exitX=0;exitY=0.75;exitDx=0;exitDy=0;" target="F6emADJ4_j-nZkKa8t7v-10" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="380" y="264" as="sourcePoint" />
            <mxPoint x="374.5" y="377" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-12" connectable="0" parent="F6emADJ4_j-nZkKa8t7v-9" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="sendNotification [SendGrid/&lt;div&gt;Twilio success]&lt;/div&gt;" vertex="1">
          <mxGeometry relative="1" x="-0.1235" y="-3" as="geometry">
            <mxPoint x="3" y="43" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-78" edge="1" parent="1" source="F6emADJ4_j-nZkKa8t7v-8" style="endArrow=open;html=1;rounded=0;align=center;verticalAlign=top;endFill=0;labelBackgroundColor=none;endSize=6;exitX=0.75;exitY=1;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;curved=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="F6emADJ4_j-nZkKa8t7v-52" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="437" y="280" as="sourcePoint" />
            <mxPoint x="581" y="389" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="F6emADJ4_j-nZkKa8t7v-79" connectable="0" parent="F6emADJ4_j-nZkKa8t7v-78" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="send/Fail" vertex="1">
          <mxGeometry relative="1" x="0.2316" y="1" as="geometry">
            <mxPoint x="-8" y="-34" as="offset" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
