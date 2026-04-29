<mxfile host="Electron" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/29.6.1 Chrome/142.0.7444.265 Electron/39.8.0 Safari/537.36" version="29.6.1">
  <diagram name="Page-1" id="9JXnoKBBeQxfI1UwHBuc">
    <mxGraphModel dx="1158" dy="731" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="077daFrloZ_0jspDVIT4-1" parent="1" style="ellipse;fillColor=strokeColor;html=1;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="430" y="100" as="geometry" />
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-4" parent="1" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="Unregistered" vertex="1">
          <mxGeometry height="40" width="120" x="380" y="200" as="geometry" />
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-5" edge="1" parent="1" style="endArrow=open;startArrow=none;endFill=0;startFill=0;endSize=8;html=1;verticalAlign=bottom;labelBackgroundColor=none;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" value="">
          <mxGeometry relative="1" width="160" as="geometry">
            <mxPoint x="439.5" y="240" as="sourcePoint" />
            <mxPoint x="440" y="360" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-7" connectable="0" parent="077daFrloZ_0jspDVIT4-5" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="register (email, password,&lt;div&gt;role) [email unique]&lt;/div&gt;" vertex="1">
          <mxGeometry relative="1" x="-0.065" y="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-8" parent="1" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="PendingVerification" vertex="1">
          <mxGeometry height="40" width="120" x="380" y="360" as="geometry" />
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-9" parent="1" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="Active" vertex="1">
          <mxGeometry height="40" width="120" x="380" y="500" as="geometry" />
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-10" parent="1" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="Deactivated" vertex="1">
          <mxGeometry height="40" width="120" x="520" y="640" as="geometry" />
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-17" parent="1" style="fontStyle=0;html=1;whiteSpace=wrap;rounded=1;" value="Suspended" vertex="1">
          <mxGeometry height="40" width="120" x="240" y="640" as="geometry" />
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-18" edge="1" parent="1" style="endArrow=open;startArrow=none;endFill=0;startFill=0;endSize=8;html=1;verticalAlign=bottom;labelBackgroundColor=none;rounded=0;" value="">
          <mxGeometry relative="1" width="160" as="geometry">
            <mxPoint x="440" y="400" as="sourcePoint" />
            <mxPoint x="440" y="500" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-19" connectable="0" parent="077daFrloZ_0jspDVIT4-18" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="verifyEmail" vertex="1">
          <mxGeometry relative="1" x="-0.065" y="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-20" edge="1" parent="1" source="077daFrloZ_0jspDVIT4-9" style="endArrow=open;startArrow=none;endFill=0;startFill=0;endSize=8;html=1;verticalAlign=bottom;labelBackgroundColor=none;rounded=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;curved=1;" value="">
          <mxGeometry relative="1" width="160" as="geometry">
            <mxPoint x="280" y="520" as="sourcePoint" />
            <mxPoint x="280.5" y="640" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-21" connectable="0" parent="077daFrloZ_0jspDVIT4-20" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="adminSuspend" vertex="1">
          <mxGeometry relative="1" x="-0.065" y="1" as="geometry">
            <mxPoint x="9" y="47" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-22" edge="1" parent="1" source="077daFrloZ_0jspDVIT4-9" style="endArrow=open;startArrow=none;endFill=0;startFill=0;endSize=8;html=1;verticalAlign=bottom;labelBackgroundColor=none;rounded=0;exitX=0.75;exitY=1;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;curved=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="077daFrloZ_0jspDVIT4-17" value="">
          <mxGeometry relative="1" width="160" as="geometry">
            <mxPoint x="439.5" y="540" as="sourcePoint" />
            <mxPoint x="440" y="660" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-23" connectable="0" parent="077daFrloZ_0jspDVIT4-22" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="adminReactivate" vertex="1">
          <mxGeometry relative="1" x="-0.065" y="1" as="geometry">
            <mxPoint x="-31" y="-38" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-24" edge="1" parent="1" source="077daFrloZ_0jspDVIT4-9" style="endArrow=open;startArrow=none;endFill=0;startFill=0;endSize=8;html=1;verticalAlign=bottom;labelBackgroundColor=none;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;edgeStyle=orthogonalEdgeStyle;curved=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="077daFrloZ_0jspDVIT4-10" value="">
          <mxGeometry relative="1" width="160" as="geometry">
            <mxPoint x="600" y="520" as="sourcePoint" />
            <mxPoint x="600.5" y="640" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-25" connectable="0" parent="077daFrloZ_0jspDVIT4-24" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="deactivateAccount" vertex="1">
          <mxGeometry relative="1" x="-0.065" y="1" as="geometry">
            <mxPoint x="-11" y="48" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-26" edge="1" parent="1" style="endArrow=open;startArrow=none;endFill=0;startFill=0;endSize=8;html=1;verticalAlign=bottom;labelBackgroundColor=none;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" value="">
          <mxGeometry relative="1" width="160" as="geometry">
            <mxPoint x="579.5" y="680" as="sourcePoint" />
            <mxPoint x="580" y="760" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-28" edge="1" parent="1" style="endArrow=open;startArrow=none;endFill=0;startFill=0;endSize=8;html=1;verticalAlign=bottom;labelBackgroundColor=none;rounded=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="077daFrloZ_0jspDVIT4-4" value="">
          <mxGeometry relative="1" width="160" as="geometry">
            <mxPoint x="439.5" y="120" as="sourcePoint" />
            <mxPoint x="439.5" y="190" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-30" parent="1" style="ellipse;html=1;shape=endState;fillColor=strokeColor;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="570" y="760" as="geometry" />
        </mxCell>
        <mxCell id="077daFrloZ_0jspDVIT4-32" parent="1" style="shape=umlFrame;whiteSpace=wrap;html=1;pointerEvents=0;recursiveResize=0;container=1;collapsible=0;width=160;" value="User Account" vertex="1">
          <mxGeometry height="790" width="560" x="157" y="35" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
